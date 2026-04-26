from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('pathway/', views.pathway, name='pathway'),
    path('institution/<int:id>/', views.institution_detail, name='institution_detail'),
    path('institutions/', views.institutions, name='institutions'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('analytics/', views.analytics, name='analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('', views.homepage, name='homepage'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('merit-calculator/', views.merit_calculator, name='merit_calculator'),
    path('pathway-advisor/', views.pathway_advisor, name='pathway_advisor'),
    path('pathway-hub/', views.pathway_hub, name='pathway_hub'),
    path('scholarship-information/', views.scholarship_information, name='scholarship_information'),
]