import requests
import os
from twilio.rest import Client

api_key = "cb4cc39ee2a35f791d63ad45ae0cf34a"
account_sid = "AC592fdffd6f2a6d7d86a36b10103eff1a"
auth_token = "d117d49543d8184d219efb8ad29bb4af"
lat = 55.755825
lon = 37.617298
weather_parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
connection = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
connection.raise_for_status()
weather_data = connection.json()
weather_codes = []
will_rain = False
for i in range(0, 12):
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]
    weather_codes.append(weather_code)

for k in weather_codes:
    if k < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to rain today, please bring an umbrella ☂ ",
        from_="+16066128473",
        to="+919354162870"
    )
    print(message.status)
