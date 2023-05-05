""" import csv

with open("testes/weather_data.csv", mode='r') as data_file:
    temperatures = []
    data = csv.reader(data_file)
    
    for row in data:
        if data.line_num != 1:
            temperatures.append(int(row[1]))
        
    print(temperatures) """
    

""" data = pandas.read_csv('testes/weather_data.csv')

temp_list = data['temp'].to_list()
print(data['temp'].mean()) #Média
print(data['temp'].max()) #Máximo

#Get a row in Data
#print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = (monday.temp * 1.8) + 32
print(monday_temp) """

""" import pandas

data = pandas.read_csv('testes/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrels_black_count = len(data[data['Primary Fur Color'] == 'Black'])
squirrels_gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
squirrels_cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

total_squirrels = {
    'Fur Color': ['Black', 'Gray', 'Cinnamon'],
    'Total': [squirrels_black_count, squirrels_gray_count, squirrels_cinnamon_count]
}

total_frame = pandas.DataFrame(total_squirrels)
total_frame.to_csv('testes/total-squirrels.csv') """

for c in range(7):
    print('o')
    
    if c == 2:
        break