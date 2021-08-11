from smtplib import SMTP_SSL
from email.message import EmailMessage
from private import gmail
from flight_data import FlightData


class NotificationManager:
    def __init__(self, ):
        self.body = ''

    def send_message(self, flight_data: FlightData, email):
        message = EmailMessage()
        self._compose_body(flight_data)
        message.set_content(self.body)
        message['Subject'] = 'Low-cost alert!'
        message['From'] = gmail.email
        message['To'] = email
        with SMTP_SSL(gmail.smtp) as connection:
            connection.login(gmail.email, gmail.password)
            connection.send_message(message)

    def _compose_body(self, flight_data: FlightData):
        self.body = (f'Only ${flight_data.price} to fly from {flight_data.from_city}-{flight_data.from_airport_code} '
                     f'to {flight_data.to_city}-{flight_data.to_airport_code}, from {flight_data.from_date} to '
                     f'{flight_data.to_date}.\n\n{flight_data.link}')
