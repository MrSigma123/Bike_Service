from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Klient'),
        ('mechanic', 'Mechanik'),
        ('warehouse', 'Magazynier'),
        ('admin', 'Administrator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class RepairRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ServiceOrder(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nowe'),
        ('diagnosis', 'Diagnoza'),
        ('in_progress', 'W trakcie'),
        ('done', 'Zakończone'),
    ]

    request = models.OneToOneField(RepairRequest, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Diagnosis(models.Model):
    order = models.OneToOneField(ServiceOrder, on_delete=models.CASCADE)
    description = models.TextField()


class RepairReport(models.Model):
    order = models.OneToOneField(ServiceOrder, on_delete=models.CASCADE)
    description = models.TextField()


class Part(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    min_quantity = models.IntegerField()


class UsedPart(models.Model):
    order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)