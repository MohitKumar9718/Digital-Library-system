# urls.py
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('student/', views.student, name="student"),
    path('seat/', views.seat, name="seat"),
    path('contact/', views.contact, name="contact"),
]
