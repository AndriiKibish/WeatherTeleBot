import requests
import json

from const import WEATHER_TOKEN, WEATHER_CITY_URL


def get_weather_city(location):
    url = WEATHER_CITY_URL.format(city=location, token=WEATHER_TOKEN)
    responce = requests.get(url)
    if responce.status_code != 200:
        return 'City not found'
    data = json.loads(responce.content)
    print(data)
    return data


def wind_direction(data: dict) ->str:
    wind_degrees = data['wind']['deg']

    if 11 < wind_degrees < 34:
        wind_dir = 'north, north-east'
    elif 34 <= wind_degrees < 56:
        wind_dir = 'north-east'
    elif 56 <= wind_degrees < 79:
        wind_dir = 'east, north-east'
    elif  79 <= wind_degrees < 101:
        wind_dir = 'east'
    elif  101 <= wind_degrees < 124:
        wind_dir = 'east, south-east'
    elif 124 <= wind_degrees < 146:
        wind_dir = 'south-east'
    elif 146 <= wind_degrees < 169:
        wind_dir = 'south, south-east'
    elif 169 <= wind_degrees < 191:
        wind_dir = 'south'
    elif 191 <= wind_degrees < 214:
        wind_dir = 'south, south-west'
    elif 214 <= wind_degrees < 236:
        wind_dir = 'south-west'
    elif 236 <= wind_degrees < 259:
        wind_dir = 'west, south-west'
    elif 259 <= wind_degrees < 281:
        wind_dir = 'west'
    elif 281 <= wind_degrees < 304:
        wind_dir = 'west, north-west'
    elif 304 <= wind_degrees < 326:
        wind_dir = 'north-west'
    elif 326 <= wind_degrees < 345:
        wind_dir = 'north, north-west'
    else:
        wind_dir = 'north'
    return wind_dir


def pars_weather_data(data:dict)->str:
    if data != "City not found":
        weather_state = data['weather'][0]['main']
        city = data['name']
        country = data['sys']['country']
        temp = round((data['main']['temp']), 1)
        wind_speed = data['wind']['speed']
        wind_dir = wind_direction(data)
        humidity = data['main']['humidity']
        pressure = round(data['main']['pressure'] / 1.333)

        msg = f'This is the weather in {city}, {country} right now:\n\t' \
              f'{weather_state}\n\t' \
              f'Temperature: {temp} °С,\n\t' \
              f'Wind: {wind_dir} {wind_speed} m/s\n\t' \
              f'Humidity: {humidity}%\n\t' \
              f'Pressure: {pressure} mm Hg\n\n' \
              f'Have a nice day!'

        return msg

    return "Sorry, but I can't find such city"