from datetime import date, timedelta
from email.message import EmailMessage
from smtplib import SMTP_SSL
from private import ALPHA_VANTAGE_TOKEN, NEWS_TOKEN, gmail, gmail_2
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE_THRESHOLD = 1
TODAY = date.today().strftime('%Y-%m-%d')
YESTERDAY = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
PRE_YESTERDAY = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')


def get_news():
    endpoint = 'https://newsapi.org/v2/everything'
    params = {'q': COMPANY_NAME,
              'from': YESTERDAY,
              'to': TODAY,
              'sortBy': 'popularity',
              'apiKey': NEWS_TOKEN}
    articles = requests.get(endpoint, params=params).json()['articles']
    return [{'title': articles[i]['title'], 'description': articles[i]['description']} for i in range(3)]


def get_stocks_change():
    endpoint = 'https://www.alphavantage.co/query'
    params = {'function': 'TIME_SERIES_DAILY',
              'symbol': STOCK,
              'apikey': ALPHA_VANTAGE_TOKEN}
    stocks = requests.get(endpoint, params=params).json()['Time Series (Daily)']
    a = float(stocks[YESTERDAY]['4. close'])
    b = float(stocks[PRE_YESTERDAY]['4. close'])
    return (a - b) / a * 100


def format_body_message():
    return '\n\n'.join([f'{i + 1}. Headline: {n["title"]}\nBrief: {n["description"]}'for i, n in enumerate(get_news())])


def send_email(title, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = title
    msg['From'] = gmail.email
    msg['To'] = gmail_2.email
    with SMTP_SSL(gmail.smtp) as connection:
        connection.login(user=gmail.email, password=gmail.password)
        connection.send_message(msg)


def main():
    positive = get_stocks_change() > CHANGE_THRESHOLD
    negative = get_stocks_change() < - CHANGE_THRESHOLD
    symbol = '🔺' * positive + '🔻' * negative
    if positive or negative:
        title = f'{STOCK}: {symbol} {get_stocks_change():.2f} %'
        body = format_body_message()
        send_email(title, body)


if __name__ == '__main__':
    main()
