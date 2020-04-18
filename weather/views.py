from django.shortcuts import render
from django.views import View
import requests

class IndexView(View):
    def get(self,request,*args,**kwargs):
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=286217dad16f0101b72bee339b6b1bcf"
        city = 'Dombivali'
        response = requests.get(url.format(city)).json()
        city_weather = {

            'city':response['name'],
            'temperature':response['main']['temp'],
            'description':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
        }

        context = {'city_weather':city_weather}
        return render(request,'weather/weather.html',context)