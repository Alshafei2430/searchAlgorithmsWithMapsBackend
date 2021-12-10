import csv
import json

def getCitiesFromCSV():
    cities = []
    with open('egyptCitiesUnicodeFormated.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cities.append(row['city'])
    with open('egyptCities.txt', 'w') as citiesfile:
        json.dump(cities, citiesfile)
    return cities

if __name__ == '__main__':
    print(getCitiesFromCSV())