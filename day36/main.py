import re
from datetime import date, timedelta
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from private import ALPHA_VANTAGE_TOKEN, NEWS_TOKEN, gmail, gmail_2
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE_THRESHOLD = 4


def get_news():
    endpoint = 'https://newsapi.org/v2/everything'
    params = {'q': COMPANY_NAME,
              'from': (date.today() - timedelta(days=1)).strftime('%Y-%m-%d'),
              'to': date.today().strftime('%Y-%m-%d'),
              'sortBy': 'popularity',
              'apiKey': NEWS_TOKEN}
    articles = requests.get(endpoint, params=params).json()['articles']
    return [{'title': articles[i]['title'], 'description': remove_links(articles[i]['description'])} for i in range(3)]


def remove_links(raw_description):
    return re.sub(r'<a href=.+</a>', '', raw_description)


def get_stocks_change():
    endpoint = 'https://www.alphavantage.co/query'
    params = {'function': 'TIME_SERIES_DAILY',
              'symbol': STOCK,
              'apikey': ALPHA_VANTAGE_TOKEN}
    stocks = requests.get(endpoint, params=params).json()['Time Series (Daily)']
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    pre_yesterday = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
    a = float(stocks[yesterday]['4. close'])
    b = float(stocks[pre_yesterday]['4. close'])
    return (a - b) / a * 100


def format_body_message():
    return '\n'.join([f'{ind + 1}. Headline: {news["title"]}\nBrief: {news["description"]}'for ind, news in enumerate(get_news())])


def send_email(title, body):
    title = title.encode('utf-8')
    body = body.encode('utf-8')
    with SMTP_SSL(gmail.smtp) as connection:
        connection.login(user=gmail.email,password=gmail.password)
        connection.sendmail(from_addr=gmail.email, to_addrs=gmail_2.email, msg=f'Subject: {title}\n\n{body}')


def main():
    if get_stocks_change() > CHANGE_THRESHOLD:
        symbol = '↑'
        title = f'{STOCK}: {symbol} {get_stocks_change():.2f} %'
        body = format_body_message()
        send_email(title, body)
    elif get_stocks_change() < - CHANGE_THRESHOLD:
        symbol = '↓'
        title = f'{STOCK}: {symbol} {get_stocks_change():.2f} %'
        body = format_body_message()
        send_email(title, body)


if __name__ == '__main__':
    main()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
