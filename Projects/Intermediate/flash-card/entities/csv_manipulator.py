import pandas as pd

class CSVManipulator:
    
    def __init__(self):
        self.df = pd.read_csv("Projects/Intermediate/flash-card/data/english_words.csv")
        self.words_dict = self.df.to_dict('records')
        print(self.words_dict)