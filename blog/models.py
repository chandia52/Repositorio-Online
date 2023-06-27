from django.db import models
import datetime


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagenes = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)