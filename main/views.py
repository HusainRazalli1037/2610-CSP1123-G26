import io
import json
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

# PDF Generation Imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Django REST Framework
from rest_framework import viewsets

# Local Model Imports
from .models import (
    Course, Visitor, Scholarship, MeritResult, University,
    PathwayHub, PathwayAdvisor, SubjectCategory, Subject,
    ScholarshipCourse, ScholarshipCriteria, ContactInquiry
)
from .serializers import ScholarshipSerializer, PathwayHubSerializer, PathwayAdvisorSerializer

# =========================
# TRACK VISITOR (UTILITY)
# =========================
def track_visit(request, page_name):
    """Logs user visits to the analytics database."""
    ip = request.META.get('REMOTE_ADDR')
    Visitor.objects.create(page=page_name, ip_address=ip)


# =========================
# BASIC PAGES
# =========================
def home(request):
    track_visit(request, 'Home')
    return render(request, 'homepages.html')

def contact(request):
    track_visit(request, 'Contact')
    return render(request, 'Contact.html')

def about_us(request):
    track_visit(request, 'About Us')
    return render(request, 'About_Us.html')


# =========================
# UNIVERSITY & PATHWAY
# =========================
def universities(request):
    track_visit(request, 'Universities')
    universities_list = University.objects.all()
    return render(request, 'universities.html', {'universities': universities_list})

def university_detail(request, id):
    university = get_object_or_404(University, id=id)
    # Using the correct related name 'university_courses' defined in models.py
    courses = Course.objects.filter(university=university)
    return render(request, 'university_detail.html', {
        'university': university,
        'courses': courses
    })

def pathway(request):
    track_visit(request, 'Pathway')
    courses = Course.objects.select_related('university').all()
    return render(request, 'pathway.html', {'courses': courses})

def pathway_advisor(request):
    track_visit(request, 'Pathway Advisor')
    
    # Fetch unique values directly from the database entries
    # This ensures if you add 'Cybersecurity' in Admin, it appears in the dropdown
    fields = PathwayAdvisor.objects.values_list('field', flat=True).distinct().order_by('field')
    locations = PathwayAdvisor.objects.values_list('location', flat=True).distinct().order_by('location')
    
    return render(request, 'Pathway_Advisor.html', {
        'fields': fields,
        'locations': locations
    })

def pathway_hub(request):
    """Renders the HTML for Pathway Hub with institution logos."""
    track_visit(request, 'Pathway Hub')
    # Use distinct university logos for the grid
    hubs = PathwayHub.objects.all()
    return render(request, 'Pathway_Hub.html', {'hubs': hubs})


# =========================
# SCHOLARSHIPS (FRONTEND & API)
# =========================
def scholarships(request):
    track_visit(request, 'Scholarships')
    scholarships_list = Scholarship.objects.all()
    return render(request, 'scholarships.html', {'scholarships': scholarships_list})

def scholarship_information(request):
    """Renders the main Info Hub (Scholarship_Information.html)."""
    track_visit(request, 'Scholarship Info Hub')
    # Prefetch related data to avoid [object Object] issues during rendering
    scholarships_list = Scholarship.objects.prefetch_related('courses', 'criteria').all()
    return render(request, 'Scholarship_Information.html', {'scholarships': scholarships_list})

def scholarship_detail(request, id):
    scholarship = get_object_or_404(Scholarship, id=id)
    # Use the related_name from models.py for cleaner queries
    courses = scholarship.courses.all()
    criterias = scholarship.criteria.all()
    return render(request, 'scholarship_detail.html', {
        'scholarship': scholarship,
        'courses': courses,
        'criterias': criterias
    })

# API ViewSets for JS fetch calls
class ScholarshipViewSet(viewsets.ModelViewSet):
    """API for myScript2.js - includes nested course/criteria names."""
    queryset = Scholarship.objects.prefetch_related('courses', 'criteria').all()
    serializer_class = ScholarshipSerializer

class PathwayHubViewSet(viewsets.ModelViewSet):
    """API for pathwayScript.js - provides university pathway data."""
    queryset = PathwayHub.objects.all()
    serializer_class = PathwayHubSerializer


class PathwayAdvisorViewSet(viewsets.ModelViewSet):
    """API endpoint for Pathway Advisor (Recommendation) data."""
    queryset = PathwayAdvisor.objects.all()
    serializer_class = PathwayAdvisorSerializer # Ensure this is created in serializers.py


# =========================
# ANALYTICS & DASHBOARD
# =========================
def analytics(request):
    total_visits = Visitor.objects.count()
    today_visits = Visitor.objects.filter(visited_at__date=date.today()).count()
    page_data = Visitor.objects.values('page').annotate(total=Count('page')).order_by('-total')

    labels = [item['page'] for item in page_data]
    totals = [item['total'] for item in page_data]

    return render(request, 'analytics.html', {
        'total_visits': total_visits,
        'today_visits': today_visits,
        'labels': labels,
        'totals': totals,
    })

@login_required
def dashboard(request):
    """Dashboard view fixing the FieldError by using correct related_name."""
    return render(request, 'dashboard.html', {
        'total_visits': Visitor.objects.count(),
        'today_visits': Visitor.objects.filter(visited_at__date=date.today()).count(),
        # Fixed: Changed 'course' to 'university_courses' to match models.py
        'universities': University.objects.annotate(total_courses=Count('university_courses')).order_by('-total_courses'),
        'popular_pages': Visitor.objects.values('page').annotate(total=Count('page')).order_by('-total'),
        'total_universities': University.objects.count(),
        'total_courses': Course.objects.count(),
        'total_scholarships': Scholarship.objects.count(),
    })


# =========================
# MERIT CALCULATOR
# =========================
def merit_calculator(request):
    if request.method == "POST":
        univ_marks = {'A+': 11.25, 'A': 10, 'A-': 8.75, 'B+': 7.5, 'B': 6.25, 'C+': 5, 'C': 3.75}
        pack_marks = {'A+': 16.88, 'A': 15, 'A-': 13.13, 'B+': 11.25, 'B': 9.38, 'C+': 7.5, 'C': 5.63}
        best_marks = {'A+': 5.63, 'A': 5, 'A-': 4.38, 'B+': 3.75, 'B': 3.13, 'C+': 2.5, 'C': 1.88}

        bm = request.POST.get("bm")
        bi = request.POST.get("bi")
        math = request.POST.get("math")
        sejarah = request.POST.get("sejarah")
        pg1 = request.POST.get("package_grade1")
        pg2 = request.POST.get("package_grade2")
        bg1 = request.POST.get("best_grade1")
        bg2 = request.POST.get("best_grade2")
        koko = float(request.POST.get("koko", 0))

        total = (
            univ_marks.get(bm, 0) + univ_marks.get(bi, 0) + univ_marks.get(math, 0) + univ_marks.get(sejarah, 0) +
            pack_marks.get(pg1, 0) + pack_marks.get(pg2, 0) +
            best_marks.get(bg1, 0) + best_marks.get(bg2, 0) + koko
        )

        # Save to DB
        MeritResult.objects.create(
            stream=request.POST.get("streamSelector"),
            bm=bm, bi=bi, math=math, sejarah=sejarah,
            package_subject1=request.POST.get("package_subject1"), package_grade1=pg1,
            package_subject2=request.POST.get("package_subject2"), package_grade2=pg2,
            best_subject1=request.POST.get("best_subject1"), best_grade1=bg1,
            best_subject2=request.POST.get("best_subject2"), best_grade2=bg2,
            koko=koko, merit=total
        )
        
        # Return result as JSON
        return JsonResponse({'result': total})

    categories = SubjectCategory.objects.prefetch_related('subjects').all()
    return render(request, "Merit_Calculator.html", {"categories": categories})


# =========================
# REPORTS & PDF EXPORT
# =========================
def reports(request):
    return render(request, 'reports.html')

def export_summary_pdf(request):
    """Generates a summary PDF report."""
    buffer = io.BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="summary_report.pdf"'

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = [Paragraph("University Pathway Summary Report", styles['Title']), Spacer(1, 20)]

    universities_list = University.objects.prefetch_related('university_courses').all()

    for uni in universities_list:
        elements.append(Paragraph(f"<b>{uni.name}</b>", styles['Heading2']))
        for course in uni.university_courses.all():
            elements.append(Paragraph(f"{course.code} - {course.name} ({course.level})", styles['BodyText']))
        elements.append(Spacer(1, 10))

    doc.build(elements)
    response.write(buffer.getvalue())
    buffer.close()
    return response

@csrf_exempt  # Only for simplicity; in production use CSRF tokens
def save_inquiry(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ContactInquiry.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                subject=data.get('subject'),
                message=data.get('message')
            )
            return JsonResponse({"status": "success"}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "invalid method"}, status=405)