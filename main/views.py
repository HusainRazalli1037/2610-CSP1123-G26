from django.shortcuts import render
from .models import Institution, Course
from .models import Visitor
from .models import Institution
from .models import Scholarship
from django.db.models import Count
from django.utils.timezone import now
from datetime import date


def institutions(request):
    track_visit(request, 'Institutions')

    institutions = Institution.objects.all()

    return render(request, 'institutions.html', {
        'institutions': institutions
    })


def home(request):
    track_visit(request, 'Home')
    return render(request, 'home.html')

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