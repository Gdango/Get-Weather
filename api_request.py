import requests
import OS
import json

access_code = os.environ['OPENWEATHER_API_ACCESS_CODE']

url = "http://api.openweathermap.org/data/2.5/forecast?q=Commerce,California&appid="+access_code

response = requests.get(url)
Data = response.json()

with open('data.txt', 'w') as outfile:
    json.dump(Data, outfile)


