import json

with open('Data.txt') as json_file:
    Data = json.load(json_file)

weather_list = Data['list']
dates = []
forecast = []

for i in range(0, len(weather_list)-1):
    try:
        dates.append(weather_list[i]['dt'])
        forecast.append(weather_list[i]['weather'][0]['main'])
    except KeyError:
        continue

print(dates)
print(forecast)


