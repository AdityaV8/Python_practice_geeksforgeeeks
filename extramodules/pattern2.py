import csv

with open("filehandling/weather.csv","r") as f:
    data = list(csv.reader(f))
    
city = input("enter a city : ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])