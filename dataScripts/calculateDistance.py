from math import *

def calculateDistance(point1, point2):
    lat1 = float(point1['lat'])
    lng1 = float(point1['lng'])
    lat2 = float(point2['lat'])
    lng2 = float(point2['lng'])
    R = 6371e3 # metres
    φ1 = lat1 * pi/180 # φ, λ in radians
    φ2 = lat2 * pi/180
    Δφ = (lat2-lat1) * pi/180
    Δλ = (lng2-lng1) * pi/180

    a = sin(Δφ/2) * sin(Δφ/2) + cos(φ1) * cos(φ2) * sin(Δλ/2) * sin(Δλ/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    d = R * c # in metres
    return d