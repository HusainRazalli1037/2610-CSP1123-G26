from django.shortcuts import render
from .models import Course
from .models import Visitor
from .models import Institution
from .models import Scholarship
from django.db.models import Count
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from .models import Visitor, Institution, Course
total_visits = Visitor.objects.count()
total_institutions = Institution.objects.count()
total_courses = Course.objects.count()

def institutions(request):
    track_visit(request, 'Institutions')

    institutions = Institution.objects.all()

    return render(request, 'institutions.html', {
        'institutions': institutions
    })

def homepage(request):
    return render(request, 'homepages.html')

def home(request):
    track_visit(request, 'Home')
    return render(request, 'homepages.html')

def about_us(request):
    return render(request, 'About_Us.html')

def calculator(request):
    track_visit(request, 'Calculator')

    result = None

    if request.method == "POST":

        nilai_gred_utama = {
            'A+': 11.25, 'A': 10, 'A-': 8.75,
            'B+': 7.5, 'B': 6.25,
            'C+': 5, 'C': 3.75,
            'D': 2.5, 'E': 1.25, 'G': 0
        }

        nilai_gred_terbaik_pakej = {
            'A+': 16.88, 'A': 15.00, 'A-': 13.13,
            'B+': 11.25, 'B': 9.38,
            'C+': 7.50, 'C': 5.63,
            'D': 3.75, 'E': 1.88, 'G': 0
        }

        nilai_gred_terbaik = {
            'A+': 5.63, 'A': 5.00, 'A-': 4.38,
            'B+': 3.75, 'B': 3.13,
            'C+': 2.50, 'C': 1.88,
            'D': 1.25, 'E': 0.63, 'G': 0
        }

        try:
            # SUBJECT UTAMA
            bm = nilai_gred_utama[request.POST['bm']]
            bi = nilai_gred_utama[request.POST['bi']]
            math = nilai_gred_utama[request.POST['math']]
            sejarah = nilai_gred_utama[request.POST['sejarah']]

            subjek_utama = [bm, bi, math, sejarah]

            # TERBAIK PAKEJ
            tp1 = nilai_gred_terbaik_pakej[request.POST['tp1']]
            tp2 = nilai_gred_terbaik_pakej[request.POST['tp2']]

            # TERBAIK
            t1 = nilai_gred_terbaik[request.POST['t1']]
            t2 = nilai_gred_terbaik[request.POST['t2']]

            koko = float(request.POST['koko'])

            skor_akademik = sum(subjek_utama) + tp1 + tp2 + t1 + t2
            jumlah_merit = skor_akademik + koko

            result = {
                "skor_akademik": round(skor_akademik, 2),
                "koko": round(koko, 2),
                "jumlah": round(jumlah_merit, 2)
            }

        except KeyError:
            result = {"error": "Gred tidak sah"}

        except ValueError:
            result = {"error": "Markah kokurikulum mesti nombor"}

    return render(request, 'calculator.html', {
        "result": result
    })


def pathway(request):
    track_visit(request, 'Pathway')

    courses = Course.objects.all()

    return render(request, 'pathway.html', {
        'courses': courses
    })


def institution_detail(request, id):
    institution = Institution.objects.get(id=id)
    courses = Course.objects.filter(institution=institution)

    return render(request, 'institution_detail.html', {
        'institution': institution,
        'courses': courses
    })


def scholarships(request):
    track_visit(request, 'Scholarships')

    scholarships = Scholarship.objects.all()

    return render(request, 'scholarships.html', {
        'scholarships': scholarships
    })


def track_visit(request, page_name):
    ip = request.META.get('REMOTE_ADDR')
    Visitor.objects.create(
        page=page_name,
        ip_address=ip
    )

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
#--------------------------------------------------

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from django.conf import settings
import os

from .models import Visitor, Institution, Course
from django.db.models import Count


def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="system_report.pdf"'

    doc = SimpleDocTemplate(response)
    elements = []
    styles = getSampleStyleSheet()

    # =========================
    # LOGO
    # =========================
    from django.contrib.staticfiles import finders
    from reportlab.platypus import Image

    logo_path = finders.find('images/logo.png')

    if logo_path:
      logo = Image(logo_path, width=100, height=100)
      elements.append(logo)

    # =========================
    # TITLE
    # =========================
    title = Paragraph("📊 SYSTEM ANALYTICS REPORT", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # =========================
    # VISITOR TREND
    # =========================
    total_visits = Visitor.objects.count()
    today_visits = Visitor.objects.filter(
        visited_at__date__isnull=False
    ).count()

    trend_data = [
        ["Total Visits", total_visits],
        ["Today Visits", today_visits],
    ]

    trend_table = Table(trend_data)
    trend_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))

    elements.append(Paragraph("📈 Visitor Trends", styles['Heading2']))
    elements.append(trend_table)
    elements.append(Spacer(1, 15))

    # =========================
    # TOP 5 COURSES
    # =========================
    top_courses = Course.objects.values('name') \
        .annotate(total=Count('id')) \
        .order_by('-total')[:5]

    course_data = [["Course", "Count"]]

    for c in top_courses:
        course_data.append([c['name'], c['total']])

    course_table = Table(course_data)
    course_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))

    elements.append(Paragraph("🏆 Top 5 Courses", styles['Heading2']))
    elements.append(course_table)
    elements.append(Spacer(1, 15))

    # =========================
    # INSTITUTIONS
    # =========================
    institutions = Institution.objects.all()

    inst_data = [["Institution", "Location"]]

    for i in institutions:
        inst_data.append([i.name, i.location])

    inst_table = Table(inst_data)
    inst_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkgreen),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))

    elements.append(Paragraph("🏫 Institutions", styles['Heading2']))
    elements.append(inst_table)

    # =========================
    # BUILD PDF
    # =========================
    doc.build(elements, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)

    return response


def draw_header_footer(canvas, doc):

    canvas.saveState()

    # =========================
    # HEADER (NAVY BLUE BANNER)
    # =========================
    canvas.setFillColor(colors.HexColor("#0d1b52"))
    canvas.rect(0, 800, 600, 50, fill=1)

    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(200, 820, "SPM SYSTEM ANALYTICS REPORT - 2026")

    # =========================
    # FOOTER
    # =========================
    canvas.setFillColor(colors.grey)
    canvas.setFont("Helvetica", 10)
    canvas.drawString(50, 30, "SPM Guideline System - Powered by Django")

    # PAGE NUMBER
    page_num = canvas.getPageNumber()
    canvas.drawString(500, 30, f"Page {page_num}")

    canvas.restoreState()


@login_required
def dashboard(request):

    total_visits = Visitor.objects.count()

    today_visits = Visitor.objects.filter(
        visited_at__date=date.today()
    ).count()

    institutions = Institution.objects.annotate(
        total_courses=Count('course')
    ).order_by('-total_courses')

    popular_pages = Visitor.objects.values('page').annotate(
        total=Count('page')
    ).order_by('-total')

    return render(request, 'dashboard.html', {
        'total_visits': total_visits,
        'today_visits': today_visits,
        'institutions': institutions,
        'popular_pages': popular_pages,
        'total_institutions': Institution.objects.count(),
        'total_courses': Course.objects.count(),
        'total_scholarships': Scholarship.objects.count(),
    })

@login_required
def reports(request):
    return render(request, 'reports.html')