from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
  
  firstName=models.CharField(max_length=100)
  lastName=models.CharField(max_length=100)
  # image=models.ImageField(upload_to='photos/%y/%m/%d')

class UploadFile(models.Model):
      name=models.CharField(max_length=100)
      file=models.FileField(upload_to='media/%y/%m/%d')
