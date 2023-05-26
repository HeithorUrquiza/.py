import requests
import os
import datetime as dt
from dotenv import load_dotenv
from entities.flight_data import FlightData

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
TIME_INTERVAL_6 = dt.timedelta(days=180)
TIME_INTERVAL_1 = dt.timedelta(days=1)

class FlightSearch:    
    
    def __init__(self) -> None:
        self.today = dt.datetime.now()
        self.tomorrow = self.today + TIME_INTERVAL_1
        self.six_mon_later = self.today + TIME_INTERVAL_6    
        
        
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
        return sheet_data
        
        
    def check_flight(self, origin_city_code, destination_city):
        api_header = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_mon_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
    
        resp = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=api_header)
        resp.raise_for_status()
        
        try:
            data = resp.json()["data"][0]
        except:
            print(f"No flights found for {destination_city}.")
            return None
        else:
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