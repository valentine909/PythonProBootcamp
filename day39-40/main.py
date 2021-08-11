from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
UPDATE_IATA = False


def update_iata_codes():
    empty_cities = data_manager.get_cities_with_empty_iata_codes()
    iata_codes = flight_search.get_iata_codes(empty_cities)
    data_manager.update_iata_codes(iata_codes)


def search_flight_deals():
    flight_requirements = data_manager.get_flights_requirements()
    return flight_search.check_destinations(flight_requirements)


if __name__ == '__main__':
    data_manager = DataManager()
    flight_search = FlightSearch()
    email_sender = NotificationManager()

    if UPDATE_IATA:
        update_iata_codes()

    flight_deals = search_flight_deals()
    if flight_deals:
        for flight in flight_deals:
            email_sender.send_message(flight)
