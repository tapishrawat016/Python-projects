import requests
from pprint import pprint

sheety_api = "https://api.sheety.co/21d7e3cebcc91392d491b86468cc3b01/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_google_sheet_data(self):
        response = requests.get(url=sheety_api)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_code(self):
        url = "https://api.sheety.co/21d7e3cebcc91392d491b86468cc3b01/flightDeals/prices"
        for city in self.destination_data:
            params = {
                "price": {
                    "iataCode": city["iataCode"]
                }

            }
            response = requests.put(url=f"{url}/{city['id']}", json=params)


