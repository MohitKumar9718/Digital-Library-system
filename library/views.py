 

# Create your views here.
from django.shortcuts import render
from .models import Student,Seat
from .forms import ContactForm
 
from collections import defaultdict
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'About.html')

def student(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'Student.html', {'students': students})

def seat(request):
    return render(request, 'Seat.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Contact.html', {'form': ContactForm(), 'success': True})
    return render(request, 'Contact.html', {'form': form})







def seat(request):
    seats = Seat.objects.all().order_by('row', 'seat_number')
    seats_by_row = defaultdict(list)
    for seat in seats:
        seats_by_row[seat.row].append(seat)
    return render(request, 'Seat.html', {'seats_by_row': dict(seats_by_row)})







 