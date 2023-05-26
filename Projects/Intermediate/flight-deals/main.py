from entities.data_manager import DataManager
from entities.flight_search import FlightSearch
from entities.notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

data_manager.get_data()

#Uso necessário apenas quando a coluna iataCode estiver vazia
#data_manager.sheet_data = flight_search.set_destination_code(data_manager.sheet_data)
#data_manager.put_data()

for row in data_manager.sheet_data:
    flight = flight_search.check_flight(origin_city_code="LON", destination_city=row["iataCode"])
    notification.send_SMS(flight=flight, lowestPrice=row["lowestPrice"]) 