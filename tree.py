import csv
import json
from getCityNeighbours import getCityNeighbours




def createTree():
    with open('egyptCitiesLat&LongUnicodeFormated.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        tree = {}

        for row in csv_reader:
            cityNeighbours = getCityNeighbours(row["city"], 10000)
            tree[row["city"]] = cityNeighbours
    with open('adjacent.txt', 'w') as outfile:
        json.dump(tree, outfile)

if __name__ == '__main__':
    createTree()