class Coordenadas:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon


coords = Coordenadas(45, 58)
coords1 = Coordenadas(45, 56)

print(coords == coords1)
