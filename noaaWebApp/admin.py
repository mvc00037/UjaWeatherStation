from django.contrib import admin

from .models import  Satellite,passSatellite, sat, imagenApt,imagen

# Register your models here.

admin.site.register(Satellite)

admin.site.register(passSatellite)

admin.site.register(sat)

class ImagenAptAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

admin.site.register(imagenApt)

admin.site.register(imagen)
