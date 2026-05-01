from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # UNIVERSITIES
    path('universities/', views.universities, name='universities'),
    path('university/<int:id>/', views.university_detail, name='university_detail'),

    # PATHWAY
    path('pathway/', views.pathway, name='pathway'),
    path('pathway-advisor/', views.pathway_advisor, name='pathway_advisor'),
    path('pathway-hub/', views.pathway_hub, name='pathway_hub'),

    # SCHOLARSHIPS
    path('scholarships/', views.scholarships, name='scholarships'),
    path('scholarship-information/', views.scholarship_information, name='scholarship_information'),
    path('scholarship/<int:id>/', views.scholarship_detail, name='scholarship_detail'),

    # SYSTEM PAGES
    path('analytics/', views.analytics, name='analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),

    # STATIC PAGES
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),

    # MERIT
    path('merit-calculator/', views.merit_calculator, name='merit_calculator'),
]