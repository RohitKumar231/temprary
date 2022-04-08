from pyexpat import model
from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=20)
    Address = models.CharField(max_length=300)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class Workers(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=300)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    service = models.CharField(max_length=100)
    # gender = models.enums{'male','female','others'}
    # charges = models.CharField(max_length=100)
    # rating = models.IntegerField()


class Appointment(models.Model):
    worker_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    Appointment_date = models.CharField(max_length=100)
    completed = models.IntegerField(default=0)
