import csv

with open('egyptCities.csv', mode='r') as csv_data:
    csv_reader = csv.DictReader(csv_data)
    line_count = 0
    with open('egyptCitiesLat&Long.csv', 'w') as egyptCitiesLatLong:
        fieldNames = ['city', "lat", "lng"]
        csv_writer = csv.DictWriter(egyptCitiesLatLong, fieldnames=fieldNames, delimiter=',')

        csv_writer.writeheader()
        for row in csv_reader:
            dic = {
                "city": row["city"],
                "lat": row["lat"],
                "lng": row["lng"],
            }
            csv_writer.writerow(dic)
