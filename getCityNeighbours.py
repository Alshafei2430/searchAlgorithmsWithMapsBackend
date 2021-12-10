import csv


def getCityNeighbours(city , zoneRedius, multiplier = 1):
    AllCityNeighbours = []
    NeighbourCitiesWithenZone = []
    NeighboursFormated = []

    with open('egypt-DistanceBetweenCitiesUnicodeFormated.csv', 'r') as csvfileR:
        csv_reader = csv.DictReader(csvfileR)
        for row in csv_reader:
            if row["from"].lower() == city.lower():
                AllCityNeighbours.append(row)
        while (len(NeighbourCitiesWithenZone) <= 3):
            for city in AllCityNeighbours:

                if(float(city["distance"]) <= zoneRedius * multiplier and (city not in NeighbourCitiesWithenZone) and float(city["distance"]) != 0):
                    NeighbourCitiesWithenZone.append(city)
            multiplier += 1
    with open('egyptCitiesLat&LongUnicodeFormated.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for city in NeighbourCitiesWithenZone:
                if row['city'] == city['to']:
                    NeighboursFormated.append(row['city'])
    return NeighboursFormated

if __name__ == "__main__":
    pass