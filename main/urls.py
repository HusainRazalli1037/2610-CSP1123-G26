from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    ScholarshipViewSet, 
    PathwayHubViewSet, 
    PathwayAdvisorViewSet, # Add this one
    export_summary_pdf
)

# 1. Setup the REST Framework Router
router = DefaultRouter()
router.register(r'scholarships', ScholarshipViewSet)
router.register(r'pathway-hub', PathwayHubViewSet) # This MUST be here for pathwayScript.js
router.register(r'pathway-advisor', PathwayAdvisorViewSet)

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # API ROOT (Serves /api/scholarships/ and /api/pathway-hub/)
    path('api/', include(router.urls)),

    # UNIVERSITIES
    path('universities/', views.universities, name='universities'),
    path('university/<int:id>/', views.university_detail, name='university_detail'),

    # PATHWAY & HUB
    path('pathway/', views.pathway, name='pathway'),
    path('pathway-advisor/', views.pathway_advisor, name='pathway_advisor'),
    path('pathway-hub/', views.pathway_hub, name='pathway_hub'),

    # SCHOLARSHIPS
    path('scholarships/', views.scholarships, name='scholarships'),
    path('scholarship-information/', views.scholarship_information, name='scholarship_information'),
    path('scholarship/<int:id>/', views.scholarship_detail, name='scholarship_detail'),

    # ANALYTICS & DASHBOARD
    path('analytics/', views.analytics, name='analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),

    # STATIC PAGES
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),

    # MERIT & EXPORTS
    path('merit-calculator/', views.merit_calculator, name='merit_calculator'),
    path('export-pdf/', export_summary_pdf, name='export_pdf'),
]

# Media support for Logos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)