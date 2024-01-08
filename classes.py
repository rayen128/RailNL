# classes

class Station():

    def __init__(self, name, y, x):
        self.name = name
        self.x = x
        self.y = y
        self.trajecten: List[Object] = []

    def add_traject(self, traject):
        self.trajecten.append(traject)


class Traject():

    def __init(self, station_1, station_2, distance):
        self.station_1 = station_1
        self.station_2 = station_2
        self.distance = distance
