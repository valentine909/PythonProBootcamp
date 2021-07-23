import requests
import datetime
from smtplib import SMTP_SSL
from time import sleep
from day32.private import gmail

MY_LAT = 53.842078
MY_LONG = 27.690238
SUNRISE_SUNSET_PARAMETERS = {'lat': MY_LAT,
                             'lng': MY_LONG,
                             'formatted': 0
                             }


def get_iss_position():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.json()['iss_position']
    longitude = data['longitude']
    latitude = data['latitude']
    return longitude, latitude


def get_sunrise_sunset_time():
    r = requests.get('https://api.sunrise-sunset.org/json', params=SUNRISE_SUNSET_PARAMETERS)
    data = r.json()['results']
    sunrise_utc_str = data['sunrise']
    sunset_utc_str = data['sunset']
    time_zone = datetime.datetime.now() - datetime.datetime.utcnow()
    sunrise = datetime.datetime.strptime(sunrise_utc_str, '%Y-%m-%dT%H:%M:%S+00:00') + time_zone
    sunset = datetime.datetime.strptime(sunset_utc_str, '%Y-%m-%dT%H:%M:%S+00:00') + time_zone
    return sunrise, sunset


def check_conditions_for_observation():
    long, lat = get_iss_position()
    sunrise, sunset = get_sunrise_sunset_time()
    curr_time = datetime.datetime.now()
    return sunset < curr_time < sunrise and MY_LAT - 5 < lat < MY_LAT + 5 and MY_LONG - 5 < long < MY_LONG + 5


def send_email():
    with SMTP_SSL(gmail.smtp) as connection:
        connection.login(user=gmail.email, password=gmail.password)
        connection.sendmail(from_addr=gmail.email,
                            to_addrs=gmail.email,
                            msg=f'Subject: ISS\n\nLook up')


def main():
    while True:
        if check_conditions_for_observation():
            send_email()
        sleep(60)


if __name__ == '__main__':
    main()
