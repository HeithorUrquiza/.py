from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()


sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
                {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
                {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
                {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
                {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
                {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
                {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
                {'city': 'San Francisco','iataCode': '','id': 9,'lowestPrice': 260},
                {'city': 'Cape Town','iataCode': '','id': 10,'lowestPrice': 378}]


data_manager = DataManager()
flight_search = FlightSearch()

data_manager.sheet_data = flight_search.set_destination_code(data_manager.sheet_data)

data_manager.put_data()


