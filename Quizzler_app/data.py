import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
connection = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_api = connection.json()
question_data = question_api["results"]
