import pandas as pd
import datetime as dt

class DatesManager:
    
    def __init__(self):
        self.df = pd.read_csv("Projects/Intermediate/birthday-wisher/birthdays.csv")
        self.dates_file = self.df.to_dict("records")
        self.current_date = dt.datetime.now()
        self.current_day = self.current_date.day
        self.current_month = self.current_date.month


    def compare_dates(self):
        for date in self.dates_file:
            if date["month"] == self.current_month and date["day"] == self.current_day:
                return date["name"], date["email"]