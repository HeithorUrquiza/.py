import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = {"Authorization": os.getenv("TOKEN")}

class DataManager:
    
    def __init__(self) -> None:
        self.sheet_data = None
        
         
    def get_data(self):
        resp = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=BEARER_TOKEN)
        data = resp.json()
        print(resp.text)
        self.sheet_data = data["prices"]
        
        
    def put_data(self):
        for dict in self.sheet_data:
            update_data = {
                "price": {
                    "iataCode": dict["iataCode"]
                }
            }
            resp = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{dict['id']}", json=update_data, headers=BEARER_TOKEN)
            resp.raise_for_status()