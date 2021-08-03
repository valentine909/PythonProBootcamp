import requests
from datetime import datetime, timedelta


TOKEN = 'hHWXwJpeKckfLFifmZiu'
USERNAME = 'valentine909'
DOMAIN = 'https://pixe.la'
HEADERS = {"X-USER-TOKEN": TOKEN}


def register_user():
    url = f'{DOMAIN}/v1/users'
    params = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
    r = requests.post(url=url, json=params)
    return True if r.json()['message'] == "Success." else False


def create_graph():
    url = f'{DOMAIN}/v1/users/{USERNAME}/graphs'
    params = {"id": "programming", "name": "Time learning CS", "unit": "hour", "type": "float", "color": "kuro"}
    r = requests.post(url=url, json=params, headers=HEADERS)
    print(r.json())


def post_data_to_graph(date, quantity):
    url = f'{DOMAIN}/v1/users/{USERNAME}/graphs/programming'
    params = {"date": date, "quantity": str(quantity)}
    r = requests.post(url=url, json=params, headers=HEADERS)
    print(r.json())


def date_format(d: datetime):
    return datetime.strftime(d, '%Y%m%d')


def update_graph_properties(graph_id, new_params):
    url = f'{DOMAIN}/v1/users/{USERNAME}/graphs/{graph_id}'
    r = requests.put(url=url, json=new_params, headers=HEADERS)
    print(r.json())


post_data_to_graph(date_format(datetime.now()), 1)
