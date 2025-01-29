from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('physics/', views.subject_files_page, {'subject': 'physics'}, name='physics'),
    path('chemistry/', views.subject_files_page, {'subject': 'chemistry'}, name='chemistry'),
    path('biology/', views.subject_files_page, {'subject': 'biology'}, name='biology'),
]