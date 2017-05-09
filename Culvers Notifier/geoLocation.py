from geopy.geocoders import Nominatim
geolocator = Nominatim()

def getCoords(city):
    coords = []
    location = geolocator.geocode(city)
    coords.append(location.latitude)
    coords.append(location.longitude)
    return coords 
