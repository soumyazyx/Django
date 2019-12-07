from django.shortcuts import render
import requests


def weather(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=491a4880b06e5a06bbeeb9630d31513a'
    r = requests.get(url).json()
    print(r)

    weather_details = {
        'city': 'London',
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    context = {'weather': weather_details}
    return render(request, 'iii_boilerplate_getjson_weather/weather.html', context)
