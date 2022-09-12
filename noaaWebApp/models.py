from django.db import models

# Create your models here.


class idSatellite(models.Model):
    name = models.CharField(max_length = 25)
    noradId = models.IntegerField(primary_key=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'SatelliteId'

class Satellite(models.Model):
    name = models.CharField(max_length=25)
    noradId = models.IntegerField(primary_key=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'Satellite'