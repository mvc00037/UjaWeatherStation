from django.contrib import admin
from django.urls import path
from noaaWebApp.views import home,prediction,prediccion,predictionNoaa19
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('predictionNoaa19/', predictionNoaa19, name='prediction'),
    path('prediccion/<str:idSat>', prediccion, name='prediccion'),
    #path('prueba/25544', prueba, name='prueba'),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)