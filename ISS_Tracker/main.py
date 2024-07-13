import time
import requests
from datetime import datetime
import smtplib

#Replace [...] with your own information
MY_LAT = [...]
MY_LONG = [...]

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if MY_LONG-5 <= iss_longitude <= MY_LONG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5 and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            # User = your google email , password = your google app password(16 letters)
            connection.login(user="[...]", password="[...]")
            connection.sendmail(from_addr="[...]", to_addrs="[...]",
                                msg="Subject: ISS TRACKER\n\nLook up! You may see the ISS")
            
