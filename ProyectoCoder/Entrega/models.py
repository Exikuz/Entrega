from django.db import models

# Create your models here.
class familia(models.Model):
    Nombre=models.CharField(max_length=30)
    edad= models.IntegerField()
    nacimiento=models.DateField()
    

