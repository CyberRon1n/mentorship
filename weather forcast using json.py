appid = '5d3393b38a00dc8a42d3f84422b4ffc5'

import json, requests, sys

if len(sys.argv) < 2:
    print('usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, appid)
response = requests.get(url)
response.raise_for_status()

weather = json.loads(response.text)

w = weatherData['list']
print('current weather in %s:'%(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('day after tomorrow')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])

