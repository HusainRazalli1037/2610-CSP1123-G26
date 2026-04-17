from django.shortcuts import render
from .models import Institution, Course

def institutions(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions.html', {
        'institutions': institutions
    })

from .models import Institution

def home(request):
    institutions = Institution.objects.all()
    return render(request, 'home.html', {
        'institutions': institutions
    })

def calculator(request):
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

            # TERBAIK PAKEJ (2 SUBJECT)
            tp1 = nilai_gred_terbaik_pakej[request.POST['tp1']]
            tp2 = nilai_gred_terbaik_pakej[request.POST['tp2']]

            subjek_terbaik_pakej = [tp1, tp2]

            # TERBAIK (2 SUBJECT)
            t1 = nilai_gred_terbaik[request.POST['t1']]
            t2 = nilai_gred_terbaik[request.POST['t2']]

            subjek_terbaik = [t1, t2]

            # KOKO
            koko = float(request.POST['koko'])

            skor_akademik = sum(subjek_utama) + sum(subjek_terbaik_pakej) + sum(subjek_terbaik)

            jumlah_merit = skor_akademik + koko

            result = {
                "skor_akademik": skor_akademik,
                "koko": koko,
                "jumlah": jumlah_merit
            }

        except KeyError:
            result = {"error": "Gred tidak sah"}
        except ValueError:
            result = {"error": "Markah kokurikulum mesti nombor"}

    return render(request, 'calculator.html', {"result": result})

def pathway(request):
    courses = Course.objects.all()

    field = request.GET.get('field')
    program = request.GET.get('program')

    if field and field != "":
        courses = courses.filter(field=field)

    if program and program != "":
        courses = courses.filter(program_type=program)

    return render(request, 'pathway.html', {'courses': courses})

from .models import Institution, Course

def institution_detail(request, id):
    institution = Institution.objects.get(id=id)
    courses = Course.objects.filter(institution=institution)

    return render(request, 'institution_detail.html', {
        'institution': institution,
        'courses': courses
    })

from .models import Scholarship

def scholarships(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'scholarships.html', {
        'scholarships': scholarships
    })