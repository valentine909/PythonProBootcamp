from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


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

    if data_manager.get_cities_with_empty_iata_codes():
        update_iata_codes()

    flight_deals = search_flight_deals()
    if flight_deals:
        for flight in flight_deals:
            for user in data_manager.get_all_emails():
                email_sender.send_message(flight, user)
