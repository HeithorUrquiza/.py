import torch
import csv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

class Analyzer():
    def __init__(self, path_save) -> None:
        self.roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.roberta)
        self.tokenizer = AutoTokenizer.from_pretrained(self.roberta)
        self.labels = ['Negative', 'Neutral', 'Positive']
        self.path_save = path_save
        
        with open(self.path_save, mode="w+", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.labels)
            writer.writeheader()


    def analyze(self, path):
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for item in csv_reader:
                text = item[0]
                encoded_text = self.tokenizer(text, return_tensors="pt")
                output = self.model(**encoded_text)
                scores = output[0][0].detach().numpy()
                scores = softmax(scores)
                
                self.save(scores)
                
                
    def save(self, data):
        with open(self.path_save, mode="a+", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.labels)
            writer.writerow({"Negative": data[0], "Neutral": data[1], "Positive": data[2]})
            

## 0.2582943,0.45127246,0.2904333 -> Represents the value of analize of null texts