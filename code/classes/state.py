from sys import argv, path
import csv

from station import Station
from connection import Connection
from route import Route


class State():
    # TODO: add "constraints satisfied" method

    def __init__(self, stations_file_path: str, connections_file_path: str, max_number_routes: int = None):
        """
        Initiates State class.
        post:
            Creates list of stations, connections and routes
            Fills list of stations and connections      
        """
        self.total_number_connections: int = 0

        # add relations to all other objects
        self.stations: list[object] = self._add_stations(stations_file_path)
        self.connections: list[object] = self._add_connections(
            connections_file_path)
        self.routes: list[object] = []

        # set number of max routes (None if there is no max)
        self.max__number_routes = max_number_routes

        # add parameters for quality score function
        self.quality: float = 0.0
        self.fraction_used_connections: float = 0.0
        self.number_routes: int = 0
        self.total_minutes: int = 0

    def _add_stations(self, file_path: str) -> list:
        """
        Adds stations from stations.csv file to the list.
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

    def _add_connections(self, file_path: str) -> list:
        """
        Adds connections from connections.csv to the list. 
        pre: 
            file path to connections.csv

        post: 
            updates total number of connections
            returns list of connection objects and adds connections to stations
        """
        with open(file_path) as connections:
            connections_reader: object = csv.DictReader(connections)

            # add connections to connections list
            connections_list: list[object] = []
            for row in connections_reader:
                assert "station1" in row.keys() and "station2" in row.keys() and "distance" in row.keys(
                ), "connections csv should have station1, station2 and distance headers"
                # look up station object by name
                station1: object = next(
                    station for station in self.stations if station.name == row["station1"])
                station2: object = next(
                    station for station in self.stations if station.name == row["station2"])

                # add connection to connection list
                new_connection: object = Connection(
                    station1, station2, float(row["distance"]))
                connections_list.append(new_connection)

                # add connection to Station objects
                for station in self.stations:
                    if station.name == row["station1"] or station.name == row["station2"]:
                        station.add_connection(new_connection)

                self.total_number_connections += 1

            return connections_list

    def _check_number_routes(self) -> bool:
        """
        Checks if the maximum number of routes is reached.
        returns:
            True if number of routes is not reached
            False otherwise    
        """
        if self.number_routes == self.max_number_routes:
            return False
        return True

    def add_route(self) -> None:
        """
        pre: 
            all data necessary for a Route object
        post: 
            creates and adds Route object to routes list
        returns:
            true if addition was succesful
            false if addition was not succesful
        """
        if self._check_number_routes():

            # add new route to list
            new_route = Route()
            self.routes.append(new_route)

            # update number of routes
            self.number_routes += 1

            return True
        else:
            return False

    def _calculate_fraction_used_connections(self) -> float:
        """
        Calculates the fraction of used connections
        post:
            updates fraction of used connections

        returns:
            newest fraction of used connections
        """
        # get number of unique connections
        unique_connections = set(
            route_connection for route in self.routes for route_connection in route.route_connections)
        number_unique_connections = len(unique_connections)

        # calculate fraction
        self.fraction_used_connections = number_unique_connections / \
            self.total_number_connections

        return self.fraction_used_connections

    def _update_number_routes(self) -> None:
        # TODO: add docstring
        # TODO: get length of list of routes
        pass

    def _calculate_total_minutes(self) -> int:
        # TODO: add docstring
        # TODO: get number of minutes from all routes
        # TODO: add numbers of minutes
        pass

    def calculate_score(self, p: float, T: int, Min=int) -> float:
        """
        post: 
            calculates and updates the quality score
        returns:
            the quality score
        """
        # TODO: update all variables with methods written above
        self.quality = self.fraction_used_connections * 10000 - \
            (self.number_routes * 100 + self.total_minutes)
        return self.quality

    def write_output(self):
        """
        Writes output to output.csv according to given standard
        post: 
            writes all routes to a .csv file
            adds score to .csv file
        """
        # TODO: write to csv
        pass


if __name__ == "__main__":
    new_state = State("../../data/stations_netherlands.csv",
                      "../../data/routes_netherlands.csv")
