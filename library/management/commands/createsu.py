from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Creates a default superuser.'

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'Mohit')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'mohitmacpherson@gmail.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Mohit9718358279@')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('✅ Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Superuser already exists'))
