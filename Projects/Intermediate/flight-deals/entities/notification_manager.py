import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
ACCOUNT_NUMBER = os.getenv("ACC_NUMBER")
PERSONAL_NUMBER = os.getenv("PSN_NUMBER")

class NotificationManager:
    
    def send_SMS(self, flight, lowestPrice):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        
        msg = f"Flight low price alert 🚨\nOnly £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}\nAccess: {flight.url} to know more about"
        
        if flight.price <= lowestPrice:
            message = client.messages.create(
                from_=f"whatsapp:{ACCOUNT_NUMBER}",
                body=msg,
                to=f"whatsapp:{PERSONAL_NUMBER}"
            )
            print("Mensagem enviada")  
        else:
            print(f"{flight.price} > {lowestPrice}")
            
            