import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = {"Authorization": os.getenv("TOKEN")}

class DataManager:
    
    def __init__(self) -> None:
        self.sheet_data = None
        
         
    def get_data(self):
        resp = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers=BEARER_TOKEN)
        data = resp.json()
        self.sheet_data = data["prices"]
        print("Data collected")
        
        
    def put_data(self):
        for dict in self.sheet_data:
            update_data = {
                "price": {
                    "iataCode": dict["iataCode"]
                }
            }
            resp = requests.put(f"{SHEETY_ENDPOINT}/prices/{dict['id']}", json=update_data, headers=BEARER_TOKEN)
            resp.raise_for_status()
            
            
    def post_user(self, user: tuple):
        add_user = {
            "user":{
                "firstName": user[0],
                "lastName": user[1],
                "email": user[2]
            }
        }
        resp = requests.post(f"{SHEETY_ENDPOINT}/users", json=add_user, headers=BEARER_TOKEN)
        resp.raise_for_status()
        print("Sucess! Your email has been added")
        
        
    def get_users(self):
        resp = requests.get(f"{SHEETY_ENDPOINT}/users", headers=BEARER_TOKEN)
        resp.raise_for_status()
        data = resp.json()["users"]
        return data