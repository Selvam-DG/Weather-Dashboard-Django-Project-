# Weather Dashboard 

A Django web application that shows weather forecasts for a given location using the OpenWeather API.

##  Features

- 7-day forecast by default
- Option to select custom day range
- Live weather data using WeatherAPI
- Deployed on Replit for public access
- 

##  Live Demo

[Click to open live demo](https://weather-dashboard-django.onrender.com)

## Project Structure
```
Weather-Dashboard-Django-Project-
├── weather_dashboard/ # Django project settings
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── dashboard/ # Main app for weather UI
│ ├── templates/
│     │ └── forecast/
│           │ └── index.html
│ ├── static/
│ │ └── forecast/
|        │ └── css/
  │           │ └── style.css
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ 
│
├── staticfiles/ # Collected static files after collectstatic
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

```

## Getting started
### 1. Clone the Repository
```bash
git clone https://github.com/Selvam-DG/Weather-Dashboard-Django-Project-.git
cd weather-dashboard
```
### 2. Create Virtual Environment
``` bash
python3 -m venv env

source env/bin/activate
```
### 3. Install Dependencies
 ``` bash
pip install -r requirements.txt
```

### 4. Set Up Environment Varaibles
> Create a .env file in the root directory and add:
```env

DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
OPENWEATHER_API_KEY=your_weathermap_api_key

```

### 5. Run the Server Locally
``` bash
python manage.py runserver
```
- Open your browser at http://127.0.0.1:8000

## License
MIT License — feel free to use, modify, and contribute.
