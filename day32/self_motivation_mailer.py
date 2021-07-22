import datetime
import smtplib
from random import choice
from private import gmail, gmail_2


def is_monday():
    return datetime.datetime.now().weekday() == 0


def get_message():
    with open('quotes.txt', encoding='utf-8') as quotes:
        return choice(quotes.readlines())


if is_monday():
    message = get_message()
    with smtplib.SMTP_SSL(gmail.smtp) as connection:
        connection.login(user=gmail.email, password=gmail.password)
        connection.sendmail(
            from_addr=gmail.email,
            to_addrs=gmail_2.email,
            msg=f'Subject: Motivation\n\n{message}')
