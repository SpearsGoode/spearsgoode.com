from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=42)
    date = models.DateField()
    image = models.ImageField(upload_to='projects/images/')
    link = models.CharField(max_length=250)
    info = models.CharField(max_length=1000)
    etc = models.CharField(max_length=100000)
