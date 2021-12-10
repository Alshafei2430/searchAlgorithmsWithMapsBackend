import requests
import csv
import getDestinations
import divide_chunks



    

def formateUrl(origin, destinations, apiKey = "<your api key>", base = "https://maps.googleapis.com/maps/api/distancematrix/json"):
    url = f"{base}?origins={origin}&destinations={destinations}&key={apiKey}"
    return url



with open('egyptCitiesLat&Long.csv', mode='r') as csv_data:
    csv_reader = csv.DictReader(csv_data)
    line_count = 0
    with open('egypt-DistanceBetweenCities.csv', 'a') as egyptCitiesLatLong:
        fieldNames = ['from', "to", "distance"]
        csv_writer = csv.DictWriter(egyptCitiesLatLong, fieldnames=fieldNames, delimiter=',')
    
        csv_writer.writeheader()
        lst = []
        for row in csv_reader:
            lst.append(row)
        
        chunks = list(divide_chunks.divide_chunks(lst, 10))
        for city in lst:
            originLat = city['lat']
            originLng = city['lng']    
            origin = f"{originLat}%2C{originLng}"
            for chunk in chunks:
                destinations = getDestinations.getDestinations(chunk)
                formatedURI = formateUrl(origin, destinations)
                response = requests.request("GET", formatedURI)
                parsedResponse = response.json()

                for i, cty in enumerate(chunk):
                    dic = {
                        "from": city["city"],
                        "to": cty["city"],
                        "distance": parsedResponse["rows"][0]["elements"][i]["distance"]["value"],
                    }
                    csv_writer.writerow(dic)
        




if __name__ == '__main__':
    pass



