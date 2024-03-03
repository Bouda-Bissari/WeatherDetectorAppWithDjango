from django.shortcuts import render
import json
import urllib.request, urllib
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7b2ceb7053530c61812d3d6b76f44c70').read()
        data = json.loads(response)
        dataj = {
            'Country_code': str(data['sys']['country']),
            'coordonnees': str(data['coord']['lon'])+' '+str(data['coord']['lat']),
            'temp': str(data['main']['temp'])+'k',
            'pression': str(data['main']['pressure']),
            'humidity': str(data['main']['humidity']),
        }

    else:
        dataj = {}
    return render(request, 'index.html',dataj)