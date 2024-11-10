from django.contrib import admin
from django.urls import path
from pages import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),  
    path('physics/', views.physics_page, name='physics'),
    path('chemistry/', views.chemistry_page, name='chemistry'),
    path('biology/', views.biology_page, name='biology'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
