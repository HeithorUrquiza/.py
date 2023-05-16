import pandas as pd
from random import choice

class CSVManipulator:
    
    def __init__(self):
        try:
            self.df = pd.read_csv("Projects/Intermediate/flash-card/data/words_to_learn.csv")
        except FileNotFoundError:
            self.df = pd.read_csv("Projects/Intermediate/flash-card/data/english_words.csv")
            self.words_to_learn = self.df.to_dict("records")
        else:
            self.words_to_learn = self.df.to_dict("records")
        
        
    def get_rand_word(self):
        new_word = choice(self.words_to_learn)
        return new_word
    
    
    def remove_word(self, dict_word):
        self.words_to_learn.remove(dict_word)
        self.df = pd.DataFrame(self.words_to_learn)
        self.df.to_csv("Projects/Intermediate/flash-card/data/words_to_learn.csv", index=False)