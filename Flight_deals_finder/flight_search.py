import requests
from flight_data import FlightData

Tequila_API = "OLFQdd08xu1O429Aq7G2rcKOGbEtcw3b"
Tequila_endpoint = "https://tequila-api.kiwi.com"


class FlightSearch:

    def iata_code(self, city_name):
        headers = {
            "apikey": Tequila_API

        }
        params = {
            "term": city_name,
            "location_types": "city",
            "locale": "en-US"

        }
        response = requests.get(url=f"{Tequila_endpoint}/locations/query", headers=headers, params=params)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_code, from_time, to_time):
        headers = {"api-key": Tequila_API

                   }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=f"{Tequila_endpoint}/v2/search", params=query, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
