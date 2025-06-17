from django.shortcuts import render
from dotenv import load_dotenv
import os, requests
from .forms import WeatherForm


load_dotenv()

continents_data  = {
    'Africa': ['Cario', 'Lagos', 'Nairobi'],
    'Europe' : ['London', 'Paris', 'Berlin'],
    'Asia':['Tokyo', 'Beijing', 'Mumbai'], 
    'North America':['New York', 'Toronto', 'Los Angeles'],
    'South America':['São Paulo', 'Buenos Aires', 'Lima'],
    'Australia': ['Sydney', 'Melbourne'],
    }

def home(request):
    weather_data = None
    error = None
    form = WeatherForm(request.POST or None)
    

    if request.method == 'POST' and form.is_valid():
        
        location = form.cleaned_data['location']
        days = form.cleaned_data['days']
        api_key = os.getenv('OPENWEATHER_API_KEY')
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"
        result = requests.get(url)
        
        if result.status_code == 200:
            weather_data = result.json()
        else: 
            error= f"API Error: {result.status_code}"
        
    return render(request, 'forecast/index.html', {'form': form, 'weather_data':weather_data, 'error': error,'continents_data':continents_data})


