from datetime import datetime
import pandas as pds
import os
from random import choice
from smtplib import SMTP_SSL
from private import gmail


def pick_random_letter():
    letter = choice(os.listdir('./letter_templates'))
    return os.path.join('letter_templates', letter)


def replace_name(name, letter):
    with open(letter, 'r', encoding='utf-8') as file:
        text = file.read().replace('[NAME]', name)
    return text


def send_mail(email, msg):
    with SMTP_SSL(gmail.smtp) as connection:
        connection.login(user=gmail.email, password=gmail.password)
        connection.sendmail(
                            from_addr=gmail.email,
                            to_addrs=email,
                            msg=f'Subject: Happy birthday\n\n{msg}'
                            )


def check_birthday():
    birth_df = pds.read_csv('birthdays.csv')
    now = datetime.now()
    for index, man in birth_df[(birth_df.day == now.day) & (birth_df.month == now.month)].iterrows():
        letter_path = pick_random_letter()
        letter = replace_name(man.names, letter_path)
        send_mail(man.email, letter)


if __name__ == '__main__':
    check_birthday()
