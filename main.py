import requests
from twilio.rest import Client
import os

WEATHER_API = os.environ["WEATHER_API"]
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
FROM_NUMBER = os.environ["FROM_NUMBER"]
TO_NUMBER = os.environ["TO_NUMBER"]
WEATHER_KEY = os.environ["WEATHER_KEY"]
LAT = 22.353176
LON = 87.333520

params = {
    "lat": LAT,
    "lon": LON,
    "key": WEATHER_KEY
}
response = requests.get(url=WEATHER_API, params=params)
response.raise_for_status()
response_data = response.json()
will_rain_happen = False
for data in response_data["data"][:12]:
    if int(data["weather"]["code"]) < 600:
        will_rain_happen = True

if will_rain_happen:
    msg = "It will rain today so, take your umbrella along with you"
else:
    msg = "It will be a bright sunny day, no rainfall today"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    from_=FROM_NUMBER,
    body=msg,
    to=TO_NUMBER
)

print(message.status)
