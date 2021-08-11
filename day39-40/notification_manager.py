from smtplib import SMTP_SSL
from email.message import EmailMessage
from private import gmail, gmail_2
from flight_data import FlightData


class NotificationManager:
    def __init__(self, ):
        self.body = None
        self.subject = 'Low-cost alert!'
        self.message = EmailMessage()

    def send_message(self, flight_data: FlightData):
        self._compose_body(flight_data)
        self.message.set_content(self.body)
        self.message['Subject'] = self.subject
        self.message['From'] = gmail.email
        self.message['To'] = gmail_2.email
        with SMTP_SSL(gmail.smtp) as connection:
            connection.login(gmail.email, gmail.password)
            connection.send_message(self.message)

    def _compose_body(self, flight_data: FlightData):
        self.body = (f'Only ${flight_data.price} to fly from {flight_data.from_city}-{flight_data.from_airport_code} '
                     f'to {flight_data.to_city}-{flight_data.to_airport_code}, from {flight_data.from_date} to '
                     f'{flight_data.to_date}.\n\n{flight_data.link}')
