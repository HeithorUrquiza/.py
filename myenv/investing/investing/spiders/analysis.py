import torch
import csv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

with open("myenv/investing/investing/spiders/data/analysisData.csv", mode="w+", newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=labels)
    writer.writeheader()

with open("myenv/investing/investing/spiders/data/translateData.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for item in csv_reader:
        text = item[0]
        encoded_text = tokenizer(text, return_tensors="pt")
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        
        with open("myenv/investing/investing/spiders/data/analysisData.csv", mode="a+", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=labels)
            writer.writerow({"Negative": scores[0], "Neutral": scores[1], "Positive": scores[2]})