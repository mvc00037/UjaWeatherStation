from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Satellite

import datetime

from .models import idSatellite

def home(request):
    sat = Satellite.objects.all()
    return render(request,'noaaWebApp/home.html', {"sat": sat})

def prediction(request):

    sat_data = []
    url = 'https://api.n2yo.com/rest/v1/satellite/radiopasses/{}/41.702/-76.014/0/2/40/&apiKey=8LTCAG-YNFHC9-K96TEM-4WW6'
    satId = '25338'

    r = requests.get(url.format(satId)).json()
    iterator = r['info']['passescount']

    for i in range(iterator):
        satResponse = {
            'satname': r['info']['satname'],
            'satId': r['info']['satid'],
            "transactionscount": r['info']['transactionscount'],
            'startAz': r['passes'][i]['startAz'],
            'endAz' : r['passes'][i]['endAz'],
            "startUTC": datetime.datetime.fromtimestamp(r['passes'][i]['startUTC'],).strftime('%Y-%m-%d %H:%M:%S'),
            "endUTC":  r['passes'][i]['endUTC'],
            "maxEl":  r['passes'][i]['maxEl'],
    }
        sat_data.append(satResponse)
    sat = Satellite.objects.all()
    print('El iterator',iterator)
    context = {'sat_data': sat_data, "sat": sat }

    return render(request,'noaaWebApp/predictionTable.html', context)



def prueba(request,idSat):
    sat_data = []
    url = 'https://api.n2yo.com/rest/v1/satellite/radiopasses/{}/41.702/-76.014/0/2/40/&apiKey=8LTCAG-YNFHC9-K96TEM-4WW6'

    r = requests.get(url.format(idSat)).json()
    iterator = r['info']['passescount']

    for i in range(iterator):
        satResponse = {
            'satname': r['info']['satname'],
            'satId': r['info']['satid'],
            "transactionscount": r['info']['transactionscount'],
            'startAz': r['passes'][i]['startAz'],
            'endAz': r['passes'][i]['endAz'],
            'maxEl' :  r['passes'][i]['maxEl'],
            "startUTC": datetime.datetime.fromtimestamp(r['passes'][i]['startUTC'], ).strftime('%Y-%m-%d %H:%M:%S'),
            "endUTC": r['passes'][i]['endUTC'],
            "maxEl": r['passes'][i]['maxEl'],
        }
        sat_data.append(satResponse)
    print('El iterator', iterator)
    context = {'sat_data': sat_data}

    return render(request, 'noaaWebApp/prueba.html', context)