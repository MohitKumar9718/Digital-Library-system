# views.py
from django.shortcuts import render

def home(request):
    return render(request, "Home.html")

def about(request):
    return render(request, "About.html")

def student(request):
    return render(request, "Student.html")

def seat(request):
    return render(request, "Seat.html")

def contact(request):
    return render(request, "Contact.html")



 

