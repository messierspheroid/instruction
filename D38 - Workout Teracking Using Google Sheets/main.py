import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "91"
HEIGHT_CM = "180"
AGE = "33"

EXERCISE_TEXT = input("Tell me which exercises you did: ")

# nutritionix
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]

# sheety
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": 0,
    "Authorization": SHEETY_TOKEN
}

nutritionix_params = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionix_response = requests.post(url=EXERCISE_ENDPOINT, json=nutritionix_params, headers=headers)
nutritionix_result = nutritionix_response.json()
print(nutritionix_result)

# test_row = ran 5k and cycled for 20 minutes

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in nutritionix_result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=headers)

    print(sheet_response.text)

# environmental variables
