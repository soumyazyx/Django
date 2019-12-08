from django.shortcuts import render
from .models import City
import requests

def home(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=491a4880b06e5a06bbeeb9630d31513a'

    # Fetch the list of cities from database
    cities = City.objects.all()
    cities_recs = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        weather_details = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        cities_recs.append(weather_details)

    return render(request, 'whatever/home.html', {'records': cities_recs})





    context = {'weather': weather_details}
    return render(request, 'iii_boilerplate_getjson_weather/weather.html', context)


