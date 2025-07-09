# library/models.py

from django.db import models

class Student(models.Model):
    FEE_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid')
    ]

    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    village_name = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    fee_status = models.CharField(max_length=10, choices=FEE_STATUS_CHOICES, default='Not Paid')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    row = models.CharField(max_length=5)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.row}-{self.seat_number}"
