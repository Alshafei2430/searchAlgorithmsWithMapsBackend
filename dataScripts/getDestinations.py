def getDestinations(cities):
    destinations = ""
    counter = 1
    for city in cities:
        destination = f"{city['lat']}%2C{city['lng']}"
        if counter != len(cities):
            destination = destination + "%7C"
        destinations = destinations + destination
        counter += 1
    return destinations