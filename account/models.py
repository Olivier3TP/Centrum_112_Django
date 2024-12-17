from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('dispatcher', 'Dyspozytor'),
        ('medic', 'Ratownik medyczny'),
    ]

    username = models.CharField(max_length=150, unique=True, primary_key=True, verbose_name='Nazwa użytkownika')
    first_name = models.CharField(max_length=30, verbose_name='Imię')
    last_name = models.CharField(max_length=30, verbose_name='Nazwisko')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='dispatcher', verbose_name='Rola')
    password = models.CharField(max_length=255, verbose_name='Hasło')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"