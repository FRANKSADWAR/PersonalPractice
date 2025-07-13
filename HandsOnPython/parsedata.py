import datetime
import json
import pprint

with open("sample-weather-history.json","r") as weather_file:
    weather_data = json.load(weather_file)

print(len(weather_data))
pprint.pp(weather_data[0])

### How many days of data do we have for each year
years = {}
for d in weather_data:
    key = d['date'][0:4]
    if key in years:
        years[key] += 1
    else:
        years[key] = 1




