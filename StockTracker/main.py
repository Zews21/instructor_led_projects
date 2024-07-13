import requests
import datetime
import smtplib

#Change STOCK and COMPANY_NAME to your own choice
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Replace [...] with your own API keys, google app password and your email
STOCK_ENDPOINT = "https://www.alphavantage.co"
stock_key = [...]
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_key = [...]
my_email = [...]
PASSWORD = [...]

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
bf_yesterday = today - datetime.timedelta(days=2)
bf_yesterday_str = bf_yesterday.strftime('%Y-%m-%d')


response = requests.get(url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&'
                            f'apikey={stock_key}')
response.raise_for_status()
data = response.json()["Time Series (Daily)"]


bf_yesterday_price = float(data[bf_yesterday_str]["4. close"])
yesterday_price = float(data[yesterday_str]["4. close"])

difference = bf_yesterday_price - yesterday_price

percent_diff = abs(difference / bf_yesterday_price * 100)

news_response = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}"
                                 f"&from={yesterday_str}&sortBy=popularity&apiKey={news_key}")
news_response.raise_for_status()
news_data = news_response.json()
news_list = news_data["articles"][slice(3)]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_list]


if percent_diff > 3 and difference > 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Stock Alert\n\n"
                                                                       f"TSLA: 🔻{round(percent_diff, 2)}%\n"
                                                                       f"{formatted_articles[0]}\n\n"
                                                                       f"{formatted_articles[1]}\n\n"
                                                                       f"{formatted_articles[2]}")
elif percent_diff > 3 and difference < 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Stock Alert\n\n"
                                                                       f"TSLA: 🔻{round(percent_diff, 2)}%\n"
                                                                       f"{formatted_articles[0]}\n\n"
                                                                       f"{formatted_articles[1]}\n\n"
                                                                       f"{formatted_articles[2]}")
