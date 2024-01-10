from sys import argv
import csv

# classes

class Map():
    
    def __init__(self, stations_file_path: str, connections_file_path: str):
        self.stations: list[object] = self.add_stations(stations_file_path)
        self.connections: list[object] = self.add_connections(connections_file_path)

    def add_stations(self, file_path: str) -> list:
        """pre: file path to stations.csv
        post: "returns list of station objects"""
        with open(file_path) as stations:
            stations_reader: object = csv.DictReader(stations)

            # add stations to the station list
            station_list: list = []
            for row in stations_reader:
                # check if columns are right
                assert "station" in row.keys() and "x" in row.keys() and "y" in row.keys(), "Station csv should have station, y and x headers"
                new_station: object = Station(row["station"], float(row["x"]), float(row["y"]))
                station_list.append(new_station)
            
            return station_list
        

    def add_connections(self, file_path: str) -> list:
        """pre: file path to connections.csv
        post: returns list of connection objects and adds connections to stations"""
        with open(file_path) as connections:
            connections_reader: object = csv.DictReader(connections)

            # add connections to connections list
            connections_list: list[object] = []
            for row in connections_reader:
                assert "station1" in row.keys() and "station2" in row.keys() and "distance" in row.keys(), "connections csv should have station1, station2 and distance headers"

                new_connection: object = Connection(row["station1"], row["station2"], float(row["distance"]))

                # add connection to connection list
                connections_list.append(new_connection)

                # add connection to Station objects
                for station in self.stations:
                    if station.name == row["station1"] or station.name == row["station2"]:
                        station.add_connection(new_connection)
            return connections_list

class Station():

    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.connections: list[object] = []

    def add_connection(self, connection: object):
        self.connections.append(connection)


class Connection():

    def __init__(self, station_1: str, station_2: str, distance: float):
        self.station_1 = station_1
        self.station_2 = station_2
        self.distance = distance

if __name__ == "__main__":

    # make sure a .csv is given for both stations and connections
    assert len(argv) == 3, "Usage: representation.py [file path stations.csv] [file path connections.csv]"

    # make Map object
    new_map: object = Map(argv[1], argv[2])
    

        