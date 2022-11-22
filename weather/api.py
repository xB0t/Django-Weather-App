from decouple import config

API_KEY = config('API_KEY')
UNITS = config('UNITS', default='metric')
api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+API_KEY+"&units="+UNITS