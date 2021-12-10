import csv
import os
from unidecode import unidecode

from ai import tree


# with open("egyptCitiesLat&Long.csv") as csv_r:
#     csv_reader = csv.DictReader(csv_r)

#     with open("egyptCitiesLat&LongUnicodeFormated.csv", "a") as csv_w:
#         csv_writer = csv.DictWriter(csv_w, fieldnames=['city', 'lat', "lng"])
#         csv_writer.writeheader()
#         for row in csv_reader:
#             csv_writer.writerow({
#                 'city': unidecode(row["city"]),
#                 'lat': row["lat"],
#                 'lng': row['lng']
#             })

tree1 = {}

for city in tree:
    neighbours = []
    for neighbour in tree[city]:
        neighbours.append(unidecode(neighbour))
    tree1[unidecode(city)] = neighbours
print(tree1)