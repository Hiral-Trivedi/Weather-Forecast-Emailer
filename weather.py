import requests

def get_weather_forecast():
    # Connecting to the weather api
    url='http://api.openweathermap.org/data/2.5/weather?q=Pune,india&APPID=e5de3ad39b39ef432e187c2a2d4de61b'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
   
    # Creating our forecast string
    forecast ='the circus forecast for today is'
    forecast +=description +' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    return(forecast)
