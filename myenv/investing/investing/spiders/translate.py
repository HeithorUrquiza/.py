import csv
from deep_translator import GoogleTranslator

newsText = []

with open("myenv/investing/investing/spiders/data/dados.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for row in csv_reader:
        translated = GoogleTranslator(source="pt", target="en").translate(text=row[0])
        newsText.append(translated)
        
        
with open("myenv/investing/investing/spiders/data/translateData.csv", mode="w+", newline='', encoding='utf-8') as csvfile:
    campo_head = ['text']
    writer = csv.DictWriter(csvfile, fieldnames=campo_head)
    
    writer.writeheader()
    for item in newsText:
        writer.writerow({"text": item})