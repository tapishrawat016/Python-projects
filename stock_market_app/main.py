import requests
from datetime import date
from datetime import timedelta
import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
yesterday = str(date.today() - timedelta(days=1))
day_before_yesterday = str(date.today() - timedelta(days=2))
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e0a41a9433ba459eaa2b7f4086fcf66a"
STOCK_API_KEY = "TS0T187QEO4VY1OD"
twilio_account_sid = "AC592fdffd6f2a6d7d86a36b10103eff1a"
twilio_auth_token = "d117d49543d8184d219efb8ad29bb4af"
stock_param = {
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY"
}
news_param = {
    "apikey": NEWS_API_KEY,
    "q": "tesla",
    "from": day_before_yesterday,
    "to": yesterday,
    "language": "en"

}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_param)
stock_data = stock_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_price = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
price_change = abs(yesterday_price - day_before_yesterday_price)
articles = []
articles_headlines = []

if price_change > (day_before_yesterday_price / 20):
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    news_data = news_response.json()
    for i in range(0, 3):
        articles.append(news_data["articles"][i]["content"])
        articles_headlines.append(news_data["articles"][i]["title"])
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK} ≥:5% \n Headline:{articles_headlines[i]}\n Brief: {articles[i]}",
            from_="+16066128473",
            to="+919354162870"
        )
        print(message.status)

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
