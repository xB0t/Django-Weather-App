from django.shortcuts import render
import requests
import json
from .api import api_url
from .models import City

def index(request):
    try:
        cities = City.objects.all()
        url = api_url

        weather_data = []

        for city in cities:  
            city_weather = requests.get(url.format(city)).json()
            weather = {
                "city" : city,
                "country": city_weather['sys']['country'],
                "temperature" : city_weather['main']['temp'],
                "description" : city_weather['weather'][0]['description'],
                "icon" : city_weather['weather'][0]['icon']
            }   
            weather_data.append(weather)

        if request.method == "POST":
            city = request.POST['city']
            if not city:
                context = {
                    "city_error":"No City Found, Please try again",
                }
                return render(request, 'index.html',context)
            else:
                response = requests.get(api_url.format(city))
                data = response.json()
                weather = {
                    "description" : data["weather"][0]["description"],
                    "icon" : data["weather"][0]["icon"]
                }
                context = {
                    "data": data,
                    "weather": weather
                }
                return render(request, 'index.html' , context)
        else:
            context = {
                "weather_data": weather_data,
            }
            return render(request, 'index.html',context)
    except:
        context = {
                "error": "Error, Please try again." 
            }
        return render(request, 'index.html', context)

    

