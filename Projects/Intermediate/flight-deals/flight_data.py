import datetime as dt
import requests

TIME_INTERVAL_6 = dt.timedelta(days=180)
TIME_INTERVAL_1 = dt.timedelta(days=1)


sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54}, {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42}, {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485}, {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551}, {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414}, {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240}, {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260}, {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}]

class FlightData:
    
    def __init__(self) -> None:
        self.today = dt.datetime.now()
        self.tomorrow = self.today + TIME_INTERVAL_1
        self.six_mon_later = self.today + TIME_INTERVAL_6

    
    def get_flight(self):
        params = {
            "fly_from": "LON",
            "fly_to": "",
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_mon_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "limit": 1
        }
        
        api_header = {
            "apikey": "-XuKk5gzuV9805nYoHVFhDaOFhx-V5Tj"
        }
        
        for item in sheet_data:
            params['fly_to'] = item["iataCode"]
            resp = requests.get("https://api.tequila.kiwi.com/v2/search", params=params, headers=api_header)
            resp.raise_for_status()
            data = resp.json()["data"][0]
            
        
            print(f"{data['cityTo']}: £{data['price']}")
    
    
f = FlightData()
f.get_flight()

