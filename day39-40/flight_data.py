from dataclasses import dataclass


@dataclass()
class FlightData:
    price: str
    from_city: str
    from_airport_code: str
    to_city: str
    to_airport_code: str
    from_date: str
    to_date: str
    link: str
