import csv
from calculateDistance import calculateDistance

with open('egyptCitiesLat&Long.csv', 'r') as csvFile:
    csv_reader = csv.DictReader(csvFile)

    with open('egypt-EstimatedDistanceBetweenCities.csv', 'a') as csvFileWr:
        fieldNames = ['from', 'to', 'distance']
        csv_writer = csv.DictWriter(csvFileWr, fieldnames=fieldNames, delimiter=',')

        csv_writer.writeheader()
        lst = []
        for row in csv_reader:
            lst.append(row)

        for city in lst:
            cityOne = {
                "lat": city['lat'],
                "lng": city['lng'],
            }
            for cty in lst:
                cityTow = {
                    "lat": cty['lat'],
                    "lng": cty['lng'],
                }
                distance = calculateDistance(cityOne, cityTow)
                dic = {
                        "from": city["city"],
                        "to": cty["city"],
                        "distance": distance,
                    }
                csv_writer.writerow(dic)
                    
        

