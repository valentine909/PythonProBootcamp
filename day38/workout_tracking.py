import os
from datetime import datetime
import requests

DOMAIN = 'https://trackapi.nutritionix.com'


def get_nutritionix_data():
    endpoint = f'{DOMAIN}/v2/natural/exercise'
    headers = {'x-app-id': os.environ['nutritionix_id'], 'x-app-key': os.environ['nutritionix_api_key'],
               'Content-Type': 'application/json'}
    params = {"query": input("Tell me what exercises you did: "),
              "gender": "male",
              "weight_kg": 91,
              "height_cm": 178,
              "age": 41}
    return requests.post(url=endpoint, headers=headers, json=params).json()["exercises"]


def parse_nutritionix_data(data: list):
    return [{'Exercise': exercise['name'].title(), 'Duration': exercise['duration_min'], 'Calories': exercise['nf_calories']}
            for exercise in data]


def post_data_to_google_sheets(data: list):
    endpoint = f'https://sheetdb.io/api/v1/{os.environ["sheetdb_workout_tracking"]}'
    for record in data:
        date = datetime.today().strftime('%d/%m/%Y')
        time_ = datetime.today().strftime('%H:%M:%S')
        data_dict = {'Date': f"\'{date}", 'Time': time_}
        data_dict.update(record)
        requests.post(url=endpoint, json=data_dict)


if __name__ == '__main__':
    post_data_to_google_sheets(parse_nutritionix_data(get_nutritionix_data()))
