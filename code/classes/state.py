from sys import argv, path
import csv

from station import Station
from connection import Connection
from route import Route


class State():

    def __init__(self, stations_file_path: str, connections_file_path: str):
        self.stations: list[object] = self.add_stations(stations_file_path)
        self.connections: list[object] = self.add_connections(
            connections_file_path)
        self.routes: list[object] = []

    def add_stations(self, file_path: str) -> list:
        """
        pre: 
            file path to stations.csv

        post: 
            returns list of station objects
        """
        with open(file_path) as stations:
            stations_reader: object = csv.DictReader(stations)

            # add stations to the station list
            station_list: list = []
            for row in stations_reader:
                # check if columns are right
                assert "station" in row.keys() and "x" in row.keys() and "y" in row.keys(
                ), "Station csv should have station, y and x headers"
                new_station: object = Station(
                    row["station"], float(row["x"]), float(row["y"]))
                station_list.append(new_station)

            return station_list

    def add_connections(self, file_path: str) -> list:
        """
        pre: 
            file path to connections.csv

        post: 
            returns list of connection objects and adds connections to stations
        """
        with open(file_path) as connections:
            connections_reader: object = csv.DictReader(connections)

            # add connections to connections list
            connections_list: list[object] = []
            for row in connections_reader:
                assert "station1" in row.keys() and "station2" in row.keys() and "distance" in row.keys(
                ), "connections csv should have station1, station2 and distance headers"

                new_connection: object = Connection(
                    row["station1"], row["station2"], float(row["distance"]))

                # add connection to connection list
                connections_list.append(new_connection)

                # add connection to Station objects
                for station in self.stations:
                    if station.name == row["station1"] or station.name == row["station2"]:
                        station.add_connection(new_connection)
            return connections_list

    def add_route(self) -> None:
        """
        pre: 
            all data necessary for a Route object

        post: 
            creates and adds Route object to routes list
        """
        new_route = Route()
        self.routes.append(new_route)

    def calculate_score(self, p: float, T: int, Min=int) -> float:
        """
        post: 
            calculates and returns the quality score
        """

        K = p * 10000 - (T * 100 + Min)
        return K

    def write_output(self):
        """
        post: 
            writes all routes to a .csv file
        """
        pass
