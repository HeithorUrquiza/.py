import requests
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = "74"
HEIGHT_CM = "166"
AGE = 21

headers = {
    "x-app-id": os.getenv("NUTRI_APP_ID"),
    "x-app-key": os.getenv("NUTRI_API_KEY"),
    "x-remote-user-id":"0"
}

params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

resp = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
print(resp.json())