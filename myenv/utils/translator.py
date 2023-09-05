import csv
from deep_translator import GoogleTranslator

class Translator():
    def __init__(self, path_save) -> None:
        self.path_save = path_save
        self.label = ['text']
        with open(self.path_save, mode="w+", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.label)
            writer.writeheader()
    
    
    def translate(self, path):
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for row in csv_reader:
                translated = GoogleTranslator(source="pt", target="en").translate(text=row[0])
                self.writeDown(translated)
            
        
    def writeDown(self, data):
        with open(self.path_save, mode="a+", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.label)
            writer.writerow({"text": data})