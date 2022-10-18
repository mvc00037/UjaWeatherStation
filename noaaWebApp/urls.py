from django.contrib import admin
from django.urls import path
from noaaWebApp.views import home,prediction,prueba,predictionNoaa19

urlpatterns = [
    path('', home, name='home'),
    path('predictionNoaa19/', predictionNoaa19, name='prediction'),
    path('prueba/<str:idSat>', prueba, name='prueba'),
    path('admin/', admin.site.urls)
]
