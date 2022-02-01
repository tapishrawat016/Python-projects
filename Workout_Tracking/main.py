import requests
from datetime import datetime

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
google_sheet_endpoint = "https://api.sheety.co/21d7e3cebcc91392d491b86468cc3b01/myWorkoutTracker/workouts"
NutritionX_API = "2e741bef0f853ab0daf9c6b7c9cbb216"
APP_ID = "9c902f4d"
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": NutritionX_API
}
exercise_query = input("Please enter the exercise you have done today")
exercise_params = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 69,
    "height_cm": 170,
    "age": 23
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = response.json()
print(exercise_data)
Date = datetime.today().strftime("%d/%m/%Y")

exercise = exercise_data["exercises"][0]["name"]
time = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]

google_sheet_header = {
    "Content-Type": "application/json"
}
google_sheet_params = {
    "workout": {
        "date": Date,
        "time": time,
        "exercise": exercise,
        "duration": time,
        "calories": calories

    }
}

google_sheet_response = requests.post(url=google_sheet_endpoint, json=google_sheet_params, headers=google_sheet_header)
print(google_sheet_response.text)
