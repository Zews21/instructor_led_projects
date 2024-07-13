import requests
from bs4 import BeautifulSoup
import smtplib
import os

url = "https://www.vivantis.ro/parfumuri/lattafa-khamrah-edp.html"
desired_price = 150
my_email = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]

response = requests.get(url=url)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")
soup.prettify()

price = float(soup.find("h3", class_="primary price").getText()[:3])
name = soup.find("h1", class_="primary text-center mb-3").getText()

if price <= desired_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Perfume price alert\n\n{name} is only {price} lei on Vivantis."
                                f" Do you think it's the right time to buy?\n"
                                f"{url}".encode("UTF-8"))
else:
    pass
