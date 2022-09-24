import zoneinfo

import pytz
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Satellite
from pytz import timezone
import datetime

from rtlsdr import RtlSdr


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
            "startUTC": datetime.datetime.utcfromtimestamp(r['passes'][i]['startUTC'],).strftime('%Y-%m-%d %H:%M:%S'),
            "endUTC":  r['passes'][i]['endUTC'],
            "maxEl":  r['passes'][i]['maxEl'],
    }
        sat_data.append(satResponse)
    sat = Satellite.objects.all()
    context = {'sat_data': sat_data, "sat": sat }


    return render(request,'noaaWebApp/predictionTable.html', context)



def prueba(request,idSat):
    sat_data = []
    url = 'https://api.n2yo.com/rest/v1/satellite/radiopasses/{}/36.76/-3.44/500/10/40/&apiKey=8LTCAG-YNFHC9-K96TEM-4WW6'

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
            "startUTC": datetime.datetime.fromtimestamp(r['passes'][i]['startUTC'],tz= pytz.timezone('Europe/Madrid')).strftime('%Y-%m-%d %H:%M:%S'),
            "endUTC": r['passes'][i]['endUTC'],
            "maxEl": r['passes'][i]['maxEl'],
        }
        #d = datetime.datetime(r['passes'][i]['startUTC'], tzinfo= zoneinfo.available_timezones('Etc/GMT+2)')
        sat_data.append(satResponse)
    context = {'sat_data': sat_data}

    return render(request, 'noaaWebApp/prueba.html', context)

def sdr():

    sdr = RtlSdr()

    # configure device
    sdr.sample_rate = 2.048e6  # Hz
    sdr.center_freq = 70e6  # Hz
    sdr.freq_correction = 60  # PPM
    sdr.gain = 'auto'

    print(sdr.read_samples(512))