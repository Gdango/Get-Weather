import json
from datetime import datetime

with open('Data.txt') as json_file:
    Data = json.load(json_file)

def Will_Rain(Data):

    weather_list = Data['list']
    date_time = [] 
    forecast = []

    for i in range(0, len(weather_list)-1):
        try:
            if weather_list[i]['weather'][0]['main'] != 'Rain':
                unix_time = weather_list[i]['dt']
                date_time.append(datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))
                forecast.append(weather_list[i]['weather'][0]['main'])
        except KeyError:
            continue

    return date_time, forecast

print(Will_Rain(Data)[0])



