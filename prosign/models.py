from django.db import models
from pyexpat import model
# Create your models here.
class verify(models.Model):
    Email = models.EmailField(unique=True)
    otp = models.CharField(max_length=50)
