import pandas as pd
from random import randint

class FilesManager:
    
    def __init__(self):
        self.df = pd.read_csv("Projects/Intermediate/birthday-wisher/birthdays.csv")
        self.letter_path = f"Projects/Intermediate/birthday-wisher/letter_templates/letter_{randint(1, 3)}.txt"
        

    def random_letter(self):
        with open(self.letter_path) as letter:
            return letter.read()
        

    def get_birthdays(self):
        birthdays_dict = {(row.month, row.day):row for index, row in self.df.iterrows()}
        return birthdays_dict