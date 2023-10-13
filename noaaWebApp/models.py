from collections import deque

from django.db import models

# Create your models here.

class passSatellite(models.Model):
    noradId = models.IntegerField(primary_key=True)
    satname = models.CharField( max_length= 50)
    transactionscount = models.IntegerField()
    startAz = models.CharField(max_length = 25)
    endAz = models.CharField(max_length = 25)
    maxEl = models.DecimalField()
    startUTC = models.CharField(max_length = 75)
    endUTC = models.CharField(max_length = 25)
    maxEl = models.CharField(max_length = 25)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'passSatellite'

class Satellite(models.Model):
    name = models.CharField(max_length=25)
    noradId = models.IntegerField(primary_key=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'Satellite'

class sat(models.Model):
    name = models.CharField(max_length=25)
    noradId = models.CharField(primary_key=True,max_length=50)
    id = models.IntegerField(primary_key= False)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'Sat'

class imagenApt(models.Model):
    Nombre = models.CharField(max_length=60)
    elevacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha =  models.DateField(auto_now_add=False)
    imagen = models.ImageField(upload_to = "media/noaaWebApp")
    audio = models.FileField(upload_to = "media/noaaWebApp", null=True)

    class Meta :
        verbose_name = 'ImagenApt'
    def _str_(self):
       return self.Nombre

class imagen(models.Model):
    Nombre = models.CharField(max_length=50)
    elevacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha =  models.DateField(auto_now=False,auto_now_add=False)
    imagen = models.ImageField()

    class Meta :
        verbose_name = 'imagen'
    def _str_(self):
       return self.Nombre