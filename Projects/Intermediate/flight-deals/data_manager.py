import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEET_ENDPOINT")

class DataManager:
    
    def __init__(self) -> None:
        self.sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
                {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
                {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
                {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
                {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
                {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
                {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
                {'city': 'San Francisco','iataCode': '','id': 9,'lowestPrice': 260},
                {'city': 'Cape Town','iataCode': '','id': 10,'lowestPrice': 378}]
        
        
    def get_data(self):
        resp = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = resp.json()
        
        
    def put_data(self):
        for dict in self.sheet_data:
            update_data = {
                "price": {
                    "iataCode": dict["iataCode"]
                }
            }
            resp = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{dict['id']}", json=update_data)
            resp.raise_for_status()
            print(resp.text)
        
        
""" f = DataManager()
f.get_data() """

