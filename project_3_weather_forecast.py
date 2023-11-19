import requests
from pprint import  pprint

API_Key = '2ee6b769d8c559ad5213b88604d6926b'

city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_Key+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
