from entities.data_manager import DataManager
from entities.flight_search import FlightSearch
from entities.notification_manager import NotificationManager
from entities.user_register import UserRegister

ORGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()
user_register = UserRegister()


while True:
    choose = input("Choose an option: [Register user / Check deals]\n").lower()

    if choose == "register user":
        new_user = user_register.add_user()
        data_manager.post_user(new_user)
        
    if choose == "check deals":
        data_manager.get_data()

        if data_manager.sheet_data[0]["iataCode"] == "":
            data_manager.sheet_data = flight_search.set_destination_code(data_manager.sheet_data)
            data_manager.put_data()

        for row in data_manager.sheet_data:
            flight = flight_search.check_flight(origin_city_code=ORGIN_CITY_CODE, destination_city=row["iataCode"])
            
            if flight == None:
                continue
            
            if flight.price < row["lowestPrice"]:
                symbol = "\xa3"
                msg = f"Flight low price alert!!\nOnly £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                
                if flight.stop_overs > 0:
                    msg += f"\n\nFlight has {flight.stop_over} stop over, via {flight.via_city}."
                
                users = data_manager.get_users()
                emails = [row["email"] for row in users]
                notification.send_SMS(msg, emails) 
        break