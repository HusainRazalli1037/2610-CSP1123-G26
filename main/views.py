from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date

from .models import Course, Visitor, Scholarship, MeritResult, University

# =========================
# TRACK VISITOR
# =========================
def track_visit(request, page_name):
    ip = request.META.get('REMOTE_ADDR')
    Visitor.objects.create(page=page_name, ip_address=ip)


# =========================
# BASIC PAGES
# =========================
def home(request):
    track_visit(request, 'Home')
    return render(request, 'homepages.html')


def contact(request):
    return render(request, 'Contact.html')


def about_us(request):
    return render(request, 'About_Us.html')


# =========================
# UNIVERSITY LIST
# =========================
def universities(request):
    track_visit(request, 'Universities')

    universities = University.objects.all()

    return render(request, 'universities.html', {
        'universities': universities
    })


def university_detail(request, id):
    university = get_object_or_404(University, id=id)
    courses = Course.objects.filter(university=university)

    return render(request, 'university_detail.html', {
        'university': university,
        'courses': courses
    })


# =========================
# PATHWAY
# =========================
def pathway(request):
    track_visit(request, 'Pathway')

    courses = Course.objects.select_related('university').all()

    return render(request, 'pathway.html', {
        'courses': courses
    })


def pathway_advisor(request):
    return render(request, 'Pathway_Advisor.html')


def pathway_hub(request):
    return render(request, 'Pathway_Hub.html')


# =========================
# SCHOLARSHIPS
# =========================
def scholarships(request):
    track_visit(request, 'Scholarships')

    scholarships = Scholarship.objects.select_related('course').all()

    return render(request, 'scholarships.html', {
        'scholarships': scholarships
    })


def scholarship_information(request):
    return render(request, 'Scholarship_Information.html')


# =========================
# ANALYTICS PAGE
# =========================
def analytics(request):
    total_visits = Visitor.objects.count()

    today_visits = Visitor.objects.filter(
        visited_at__date=date.today()
    ).count()

    page_data = Visitor.objects.values('page').annotate(
        total=Count('page')
    ).order_by('-total')

    labels = [item['page'] for item in page_data]
    totals = [item['total'] for item in page_data]

    return render(request, 'analytics.html', {
        'total_visits': total_visits,
        'today_visits': today_visits,
        'labels': labels,
        'totals': totals,
    })


# =========================
# DASHBOARD (FIXED)
# =========================
@login_required
def dashboard(request):

    total_visits = Visitor.objects.count()

    today_visits = Visitor.objects.filter(
        visited_at__date=date.today()
    ).count()

    universities = University.objects.annotate(
        total_courses=Count('course')
    ).order_by('-total_courses')

    popular_pages = Visitor.objects.values('page').annotate(
        total=Count('page')
    ).order_by('-total')

    return render(request, 'dashboard.html', {
        'total_visits': total_visits,
        'today_visits': today_visits,
        'universities': universities,
        'popular_pages': popular_pages,
        'total_universities': University.objects.count(),
        'total_courses': Course.objects.count(),
        'total_scholarships': Scholarship.objects.count(),
    })

# =========================
# MERIT CALCULATOR
# =========================
def merit_calculator(request):

    result = None

    if request.method == "POST":

        universalMarks = {
            'A+': 11.25, 'A': 10, 'A-': 8.75,
            'B+': 7.5, 'B': 6.25,
            'C+': 5, 'C': 3.75
        }

        packageMarks = {
            'A+': 16.88, 'A': 15, 'A-': 13.13,
            'B+': 11.25, 'B': 9.38,
            'C+': 7.5, 'C': 5.63
        }

        bestMarks = {
            'A+': 5.63, 'A': 5, 'A-': 4.38,
            'B+': 3.75, 'B': 3.13,
            'C+': 2.5, 'C': 1.88
        }

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
            universalMarks.get(bm, 0) +
            universalMarks.get(bi, 0) +
            universalMarks.get(math, 0) +
            universalMarks.get(sejarah, 0) +
            packageMarks.get(pg1, 0) +
            packageMarks.get(pg2, 0) +
            bestMarks.get(bg1, 0) +
            bestMarks.get(bg2, 0) +
            koko
        )

        MeritResult.objects.create(
            stream=request.POST.get("streamSelector"),
            bm=bm,
            bi=bi,
            math=math,
            sejarah=sejarah,
            package_subject1=request.POST.get("package_subject1"),
            package_grade1=pg1,
            package_subject2=request.POST.get("package_subject2"),
            package_grade2=pg2,
            best_subject1=request.POST.get("best_subject1"),
            best_grade1=bg1,
            best_subject2=request.POST.get("best_subject2"),
            best_grade2=bg2,
            koko=koko,
            merit=total
        )

        result = total

    return render(request, "Merit_Calculator.html", {"result": result})

def reports(request):
    return render(request, 'reports.html')

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    doc = SimpleDocTemplate(response)
    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("System Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    doc.build(elements)

    return response