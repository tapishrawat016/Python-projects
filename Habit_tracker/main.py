import requests
from datetime import datetime

USERNAME = "tapish"
TOKEN = "ajxhuwhd72871hdiuwqhd9q"
endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=endpoint,json=user_params)
# print(response.text)
graph_endpoint = f"{endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "running graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"

}

headers = {
    "X-USER-Token": TOKEN
}
today = datetime.now()

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today")
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_response = requests.post(url=f"{graph_endpoint}/graph1", json=post_pixel_params, headers=headers)
# pixel_update = requests.put(url=f"{graph_endpoint}/graph1/{date}", json=post_pixel_params, headers=headers)
# pixel_delete = requests.delete(url=f"{graph_endpoint}/graph1/{date}", headers=headers)
print(pixel_response.text)
