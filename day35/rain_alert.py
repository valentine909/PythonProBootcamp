import requests
import json
from private import TOKEN, OWM_TOKEN


def pushbullet_message(title, body):
    message = {'type': 'note',
               'title': title,
               'body': body}
    r = requests.post('https://api.pushbullet.com/v2/pushes',
                  data=json.dumps(message),
                  headers={'Authorization': 'Bearer' + TOKEN,
                           'Content-Type': 'application/json'})
    if r.status_code != 200:
        print(r.status_code)
        raise Exception('Error', r.status_code)
    else:
        print('Message sent')


def get_weather_data():
    owm_endpoint = f'https://api.openweathermap.org/data/2.5/onecall'
    weather_params = {"lat": '53.842078',
                      "lon": '27.690238',
                      "appid": OWM_TOKEN,
                      "exclude": 'current,minutely,daily'}
    r = requests.get(owm_endpoint, params=weather_params)
    r.raise_for_status()
    hourly_weather_12 = [r.json()['hourly'][i]['weather'][0]['id'] for i in range(12)]
    print(hourly_weather_12)
    if any([x < 600 for x in hourly_weather_12]):
        pushbullet_message('It\'ll be raining', 'Take an umbrella')


if __name__ == '__main__':
    get_weather_data()
