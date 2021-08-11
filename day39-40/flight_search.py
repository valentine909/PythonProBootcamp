from datetime import timedelta, datetime
import requests
from private import FLIGHT_TOKEN
from flight_data import FlightData

NIGHTS_FROM = '7'
NIGHTS_TO = '28'
SEARCH_LIMIT = '1'
CURRENCY = 'USD'


class FlightSearch:
    def __init__(self):
        self.headers = {'apikey': FLIGHT_TOKEN}
        self.locations_endpoint = f'https://tequila-api.kiwi.com/locations/query'
        self.flights_endpoint = f'https://tequila-api.kiwi.com/v2/search'

    def check_destinations(self, destinations_list: list[FlightData]) -> list[FlightData]:
        results = []
        for flight in destinations_list:
            params = {'fly_from': flight.from_airport_code,
                      'fly_to': flight.to_airport_code,
                      'curr': CURRENCY,
                      'date_from': flight.from_date,
                      'date_to': flight.to_date,
                      'nights_in_dst_from': NIGHTS_FROM,
                      'nights_in_dst_to': NIGHTS_TO,
                      'price_to': flight.price,
                      'limit': SEARCH_LIMIT}
            r = requests.get(self.flights_endpoint, headers=self.headers, params=params)
            if r.status_code == 200 and r.json()['data']:
                data = r.json()['data'][0]
                from_date = datetime.strptime(data['local_departure'].split('T')[0], '%Y-%m-%d')
                to_date = from_date + timedelta(days=int(data['nightsInDest']))
                results.append(FlightData(from_airport_code=data['flyFrom'],
                                          from_city=data['cityFrom'],
                                          from_date=from_date.strftime('%d/%m/%Y'),
                                          to_city=data['cityTo'],
                                          to_airport_code=data['flyTo'],
                                          to_date=to_date.strftime('%d/%m/%Y'),
                                          price=data['price'],
                                          link=data['deep_link']))
        return results

    def get_iata_codes(self, cities_list: list) -> dict:
        iata_codes = {}
        for city in cities_list:
            r = requests.get(self.locations_endpoint, headers=self.headers, params={'term': f'{city}'})
            iata_codes[city] = r.json()['locations'][0]['code']
        return iata_codes

