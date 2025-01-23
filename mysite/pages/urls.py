from django.contrib import admin
from django.urls import path
from pages import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='index'),  
    path('physics/', views.physics_page, name='physics'),
    # path('chemistry/', views.chemistry_page, name='list'),
    # path('biology/', views.biology_page, name='list'),
    # path('about/', views.about_page, name='list'),
]