import requests
import os
import datetime as dt
from dotenv import load_dotenv

GENDER = "male"
WEIGHT_KG = "74"
HEIGHT_CM = "166"
AGE = 21

class SheetsManager:
    
    def __init__(self) -> None:
        load_dotenv()
        self.nutri_auth = {
            "x-app-id": os.getenv("NUTRI_APP_ID"),
            "x-app-key": os.getenv("NUTRI_API_KEY"),
            "x-remote-user-id":"0"
        }
        self.params = {
            "query": input("Tell me which exercises you did: "),
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE
        }
        self.workouts = {
            "workout": {}
        }
        self.bearer_token = {
            "Authorization": os.getenv("TOKEN")
        }
        self.today = dt.datetime.now()
        self.today_date = self.today.date()
        self.today_hr = self.today.time()
        
        
    def get_exercises(self):
        resp = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=self.params, headers=self.nutri_auth)
        data = resp.json()
        
        return data
        
        
    def exercises_register(self):
        data = self.get_exercises()
        for exercise in data['exercises']:
            self.workouts["workout"]["date"] = self.today_date.strftime("%d/%m/%Y")
            self.workouts["workout"]["time"] = self.today_hr.strftime("%X")
            self.workouts["workout"]["exercise"] = exercise["name"].title()
            self.workouts["workout"]["duration"] = exercise["duration_min"]
            self.workouts["workout"]["calories"] = exercise["nf_calories"]
            
            resp2 = requests.post(url=os.getenv("SHEET_ENDPOINT"), json=self.workouts, headers=self.bearer_token)
            print(resp2.json()) 