from django.db import models
from .constants import PhoneType


class Contact(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=13)
    contacts = models.ForeignKey('Contact', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=PhoneType.choice())

    def __str__(self):
        return self.number
