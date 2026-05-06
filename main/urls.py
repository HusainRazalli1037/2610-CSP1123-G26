from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# Import specific view functions if they aren't handled by the 'views' module alias
from .views import export_summary_pdf, ScholarshipViewSet

# 1. Setup the REST Framework Router
router = DefaultRouter()
router.register(r'scholarships', ScholarshipViewSet)

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # API ROOT
    # This provides the endpoint: /api/scholarships/ used in myScript2.js
    path('api/', include(router.urls)),

    # UNIVERSITIES
    path('universities/', views.universities, name='universities'),
    path('university/<int:id>/', views.university_detail, name='university_detail'),

    # PATHWAY
    path('pathway/', views.pathway, name='pathway'),
    path('pathway-advisor/', views.pathway_advisor, name='pathway_advisor'),
    path('pathway-hub/', views.pathway_hub, name='pathway_hub'),

    # SCHOLARSHIPS
    path('scholarships/', views.scholarships, name='scholarships'),
    # This handles the template Scholarship_Information.html
    path('scholarship-information/', views.scholarship_information, name='scholarship_information'),
    path('scholarship/<int:id>/', views.scholarship_detail, name='scholarship_detail'),

    # SYSTEM PAGES & ANALYTICS
    path('analytics/', views.analytics, name='analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),

    # STATIC PAGES
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),

    # MERIT & EXPORTS
    path('merit-calculator/', views.merit_calculator, name='merit_calculator'),
    # Use export_summary_pdf and ensure name is unique if export_pdf is different
    path('export-pdf/', export_summary_pdf, name='export_pdf'),
]