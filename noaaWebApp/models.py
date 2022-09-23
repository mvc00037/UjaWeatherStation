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