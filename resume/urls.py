from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('extract_resume/', views.extract_resume, name='extract_resume'),
]