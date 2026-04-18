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
]