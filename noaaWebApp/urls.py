from django.contrib import admin
from django.urls import path
from noaaWebApp.views import home,prediction,prueba

urlpatterns = [
    path('', home, name='home'),
    path('prediction', prediction, name='prediction'),
    path('prueba/<str:idSat>', prueba, name='prueba'),
    path('admin/', admin.site.urls)
]
