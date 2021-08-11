import requests
from datetime import datetime, timedelta
from private import SHEETDB_TOKEN
from flight_data import FlightData
FROM_CITY = 'London'
FROM_CODE = 'LON'


class DataManager:
    def __init__(self):
        self.endpoint = f'https://sheetdb.io/api/v1/{SHEETDB_TOKEN}'
        self.flight_data = requests.get(self.endpoint)
        self.tomorrow = (datetime.today() + timedelta(days=1)).strftime('%d/%m/%Y')
        self.half_year = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')

    def get_flights_requirements(self) -> list:
        search_data = []
        for city in self.flight_data.json():
            search_data.append(FlightData(from_airport_code=FROM_CODE,
                                          from_city=FROM_CITY,
                                          from_date=self.tomorrow,
                                          to_city=city['City'],
                                          to_airport_code=city['IATA Code'],
                                          to_date=self.half_year,
                                          price=city['Lowest Price'],
                                          link=''))
        return search_data

    def get_cities_with_empty_iata_codes(self):
        return [city['City'] for city in self.flight_data.json() if city['IATA Code'] == '']

    def update_iata_codes(self, city_code_dict: dict):
        for key, value in city_code_dict.items():
            update_endpoint = f'{self.endpoint}/City/{key}'
            requests.patch(update_endpoint, json={'IATA Code': value})
        self.flight_data = requests.get(self.endpoint)

    def register_new_user(self, first_name, last_name, email):
        params = {'sheet': 'users'}
        data = {'First Name': first_name, 'Last Name': last_name, 'Email': email}
        requests.post(self.endpoint, json=data, params=params)

    def get_all_emails(self):
        params = {'sheet': 'users'}
        return [user['Email'] for user in requests.get(self.endpoint, params=params).json()]
