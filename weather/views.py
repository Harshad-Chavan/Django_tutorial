from django.shortcuts import render,reverse,redirect
from django.views import View
import requests
from .models import City
from .forms import CityForm

class IndexView(View):
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=286217dad16f0101b72bee339b6b1bcf"
    def get(self,request,*args,**kwargs):
        print(args)
        # print("message = {}".format(self.message))
        cities = City.objects.all()
        form = CityForm()
        weather_data = []
        for city in cities:
            response = requests.get(self.url.format(city)).json()
        
            city_weather = {

                'city':response['name'],
                'temperature':response['main']['temp'],
                'description':response['weather'][0]['description'],
                'icon':response['weather'][0]['icon'],
            }

            weather_data.append(city_weather)

        
        context = {'weather_data':weather_data,'form':form,
                    'message':'hello','message_class':''}
        return render(request,'weather/weather.html',context)
    
    def post(self,request,*args,**kwargs):
        
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            count = City.objects.filter(name=new_city).count()
            if count == 0:
                response = requests.get(self.url.format(new_city)).json()
                if response['cod'] == 200:
                    form.save()
                    message = "City added successfully "
                    message_class = 'is-success'
                else:
                    message = "City does not exist int the world! "
                    message_class = 'is-danger'
            else:
                message = "City already exist in database"
                message_class = 'is-danger'
        return redirect(permanent=True,to="index")
