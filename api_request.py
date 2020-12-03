import requests
import access
import json


url = "http://api.openweathermap.org/data/2.5/forecast?q=Commerce,California&appid="+access.access_code()

response = requests.get(url)
Data = response.json()

with open('data.txt', 'w') as outfile:
    json.dump(Data, outfile)


