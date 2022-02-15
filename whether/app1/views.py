from django.shortcuts import render
import urllib.request
import json
from django.http import JsonResponse


# Create your views here.

def home(request):
    if request.is_ajax and request.method == 'POST':
        city = request.POST['city']
        print(city)

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=1ef0ab6eaaff1737254419c9a5da8cf4').read()

        # convert  json file into python dictionary
        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'temp': str(list_of_data["main"]['temp']),
            'pressure': str(list_of_data['main']["pressure"]),
            'humidity': str(list_of_data['main']['humidity']),
            'temp_min': str(list_of_data['main']['temp_min']),
            'speed': str(list_of_data['wind']['speed']),
            'description': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city
        }
        return render(request, 'app1/whether.html', data)

    data = {}
    return render(request, 'app1/whether.html', data)


