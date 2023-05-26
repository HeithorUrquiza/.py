import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
                {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
                {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
                {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
                {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
                {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
                {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
                {'city': 'San Francisco','iataCode': '','id': 9,'lowestPrice': 260},
                {'city': 'Cape Town','iataCode': '','id': 10,'lowestPrice': 378}]



class FlightSearch:        
        
    def get_destination_code(self, city_name: str):
        params = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        
        api_header = {
            "apikey": TEQUILA_API_KEY
        }
        
        resp = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=api_header)
        resp.raise_for_status()
        code = resp.json()["locations"][0]["code"]
        return code
        
        
    def set_destination_code(self, sheet_data: list):
        for dict in sheet_data:
            iataCODE = self.get_destination_code(dict["city"])
            if dict["iataCode"] == "":
                dict["iataCode"] = iataCODE
        print (sheet_data)
        
        
f = FlightSearch()
f.set_destination_code(sheet_data)
    