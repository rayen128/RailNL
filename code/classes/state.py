import csv
import sys
import copy
import os

sys.path.append("code/classes")
from station import Station
from connection import Connection
from route import Route


class State():

    def __init__(self, stations_file_path: str,
                 connections_file_path: str,
                 max_number_routes: int,
                 time_frame: int,
                 relaxed_all_connections: bool = False,
                 relaxed_max_routes: bool = False,
                 relaxed_time_frame: bool = False):
        """
        Initiates State class.

        pre:
            max number of routes is greater than 0
            timeframe is greater than 0

        post:
            Creates list of stations, connections and routes
            Fills list of stations and connections
            Creates constraint relaxation variables
        """
        assert max_number_routes > 0, \
            "Max number of routes should be greater than 0"
        assert time_frame > 0, \
            "Timeframe should be greater than 0"

        self.total_number_connections: int = 0

        # add relations to all other objects
        self.stations: list['Station'] = self._add_stations(stations_file_path)
        self.connections: list['Connection'] = self._add_connections(
            connections_file_path)
        self.routes: list['Route'] = []

        self.max_number_routes: int = int(max_number_routes)
        self.time_frame: int = time_frame

        # add parameters for quality score function
        self.score: float = 0.0
        self.fraction_used_connections: float = 0.0
        self.number_routes: int = 0
        self.total_minutes: int = 0

        # variables for constraint relaxation
        self.relaxed_all_connections = relaxed_all_connections
        self.relaxed_time_frame = relaxed_time_frame
        self.relaxed_max_routes = relaxed_max_routes

        # route id tracker for defining the name of a route
        self.route_id_tracker: int = 1

        # connection usage lists are for checking if all connections are used,
        # and can be used to only add unused connections
        self.used_connections: list = []
        self.unused_connections: list = [
            connection for connection in self.connections]

    def __str__(self):
        """
        Gives description of the state object

        returns:
            description of the state object
        """
        return (f"State object with score {self.calculate_score()}")

    def _add_stations(self, file_path: str) -> list['Station']:
        """
        Returns stations from stations.csv

        pre:
            file path to stations.csv exists

        returns:
            list of Station objects
        """
        assert os.path.exists(file_path), f"path {file_path} does not exist."

        with open(file_path) as stations:
            stations_reader: 'csv.DictReader' = csv.DictReader(stations)

            # add stations to the station list
            station_list: list = []
            for row in stations_reader:

                # check if columns are right
                assert "station" in row.keys() and \
                    "x" in row.keys() and \
                    "y" in row.keys(), \
                    "Station csv should have station, y and x headers"

                # create new Station object
                new_station: 'Station' = Station(
                    row["station"], float(row["x"]), float(row["y"]))
                station_list.append(new_station)

            return station_list

    def _add_connections(self, file_path: str) -> list:
        """
        Returns connections from connections.csv

        pre:
            file path to connections.csv exists

        post:
            updates total number of connections
            adds connections to stations from stations list

        returns:
            list of Connection objects
        """
        assert os.path.exists(file_path), f"path {file_path} does not exist."

        with open(file_path) as connections:
            connections_reader: 'csv.DictReader' = csv.DictReader(connections)
            connections_list: list['Connection'] = []

            for row in connections_reader:

                # check if columns are right
                assert "station1" in row.keys() and \
                    "station2" in row.keys() and \
                    "distance" in row.keys(), \
                    "csv should have station1, station2 and distance headers"

                # look up Station objects by name
                station1: 'Station' = next(
                    station for station in self.stations
                    if station.name == row["station1"])
                station2: 'Station' = next(
                    station for station in self.stations
                    if station.name == row["station2"])

                # add connection to connection list
                new_connection: 'Connection' = Connection(
                    self.total_number_connections,
                    station1,
                    station2,
                    float(row["distance"]))
                connections_list.append(new_connection)

                # add connection to Station objects
                for station in self.stations:
                    if (
                            station.name == row["station1"] or
                            station.name == row["station2"]
                    ):
                        station.add_connection(new_connection)

                # update number of connections
                self.total_number_connections += 1

            return connections_list

    def _check_number_routes(self) -> bool:
        """
        Checks if the maximum number of routes is reached.

        returns:
            True if number of routes is not reached, and
            if max routes constraint is relaxed
            False otherwise
        """
        if (
                not self.relaxed_max_routes and
                self.number_routes == self.max_number_routes
        ):
            return False
        return True

    def add_route(self, connection: 'Connection') -> bool:
        """
        Adds a new route.

        post:
            creates and adds Route object to routes list

        returns:
            true if addition was succesful
            false if addition was not succesful
        """

        # if max number of routes is not reached
        if self._check_number_routes():

            # determine route name, using id tracker
            name = f"train_{self.route_id_tracker}"
            self.route_id_tracker += 1

            # add new route to list
            new_route = Route(name, connection)
            self.routes.append(new_route)

            # update number of routes
            self.number_routes += 1

            self.set_used(connection)

            return True
        else:
            return False

    def delete_route(self, route: 'Route'):
        """
        Deletes given route

        post:
            removes route from routes list

        returns:
            True if operation was succesful
        """
        if route in self.routes:

            # fetch all connections in route
            connections = copy.copy(route.route_connections)

            self.routes.remove(route)

            # update connection usage variables
            for connection in connections:
                connection.used -= 1
                self.set_unused(connection)

            self._update_number_routes()

            return True
        else:
            return False

    def set_used(self, connection: 'Connection') -> None:
        """
        Moves connection from unused to used connections

        post:
            removes connection from unused connections list
            adds connection to used connections list
        """
        if connection in self.unused_connections:
            self.unused_connections.remove(connection)
            self.used_connections.append(connection)

    def set_unused(self, connection: 'Connection') -> None:
        """
        Moves connection from used to unused connections

        post:
            removes connection from used connections list (if not in any route)
            adds connection to unused connections list (if not in any route)
        """

        # removal does not work if the connection is not in used_connections
        if connection in self.used_connections:

            # check if connection is not in any route
            if not any(route
                       for route in self.routes
                       if connection in route.route_connections):
                self.used_connections.remove(connection)
                self.unused_connections.append(connection)

    def add_connection_to_route(self,
                                route: 'Route',
                                connection: 'Connection') -> bool:
        """
        Adds given connection to given route, if possible

        post:
            Given connection is added to given route
            used_connections and unused_connections are updated

        returns:
            True if action is successfull,
            False otherwise
        """

        # add_connection implicitly adds the connection if possible
        if route.add_connection(connection):
            self.set_used(connection)
            return True
        return False

    def delete_end_connection_from_route(self, route: 'Route') -> bool:
        """
        deletes last connection of given route

        pre:
            route is in routes list
            route is not empty

        post:
            deletes end connection of given route
            updates usage of deleted connection

        returns:
            boolean indicating successfulness of operation
        """
        assert route in self.routes, \
            "Route not in routes list of current state"
        assert len(route.route_connections) != 0, \
            "Route is empty already"

        connection = route.route_connections[-1]

        # method implicitly deletes end connection
        if route.delete_connection_end():
            self.set_unused(connection)
            return True
        return False

    def delete_start_connection_from_route(self, route: 'Route') -> bool:
        """
        deletes first connection of given route

        pre:
            route is in routes list
            route is not empty

        post:
            deletes start connection of given route
            updates usage of deleted connection

        returns:
            boolean indicating successfulness of operation
        """
        assert route in self.routes, \
            "Route not in routes list of current state"
        assert len(route.route_connections) != 0, \
            "Route is empty already"

        connection = route.route_connections[0]

        # method implicitly deletes start connection
        if route.delete_connection_start():
            self.set_unused(connection)
            return True
        return False

    def _update_fraction_used_connections(self) -> float:
        """
        Calculates the fraction of used connections

        post:
            updates fraction of used connections

        returns:
            newest fraction of used connections
        """
        # get number of unique connections
        unique_connections = set(
            route_connection
            for route in self.routes
            for route_connection in route.route_connections)
        number_unique_connections = len(unique_connections)

        # calculate fraction
        self.fraction_used_connections = number_unique_connections / \
            self.total_number_connections

        return self.fraction_used_connections

    def _update_number_routes(self) -> int:
        """
        Updates the number of routes.

        post:
            updates number of routes

        returns:
            number of routes
        """
        self.number_routes = len(self.routes)
        return self.number_routes

    def _update_total_minutes(self) -> int:
        """
        Calculates total number of minutes of all routes.

        post:
            updates total number of minutes

        returns:
            total number of minutes
        """

        # calculate number of minutes
        self.total_minutes = sum(
            connection.distance
            for route in self.routes
            for connection in route.route_connections)

        return self.total_minutes

    def calculate_score(self) -> float:
        """
        post:
            calculates and updates the quality score
        returns:
            the quality score
        """
        # update all variables with methods written above
        self._update_number_routes()
        self._update_fraction_used_connections()
        self._update_total_minutes()

        # score function: k = p * 10000 - (100T + Min)
        self.score = self.fraction_used_connections * 10000 - \
            (self.number_routes * 100 + self.total_minutes)

        return self.score

    def write_output(self, file_path: str) -> None:
        """
        Writes output to output.csv according to given standard:
            train name, list of stations
            last line: 'score', score

        post:
            writes all routes to a .csv file
            adds score to .csv file
        """

        # code source:
        #   https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            # write column headers
            writer.writerow(['train', 'stations'])

            # write stations
            for route in self.routes:
                new_row: list = []
                new_row.append(route.name)

                stations_str: str = "[" + ", ".join(
                    station.name for station in route.route_stations) + "]"

                new_row.append(stations_str)
                writer.writerow(new_row)

            # write score
            writer.writerow(["score", self.calculate_score()])

    def routes_valid_time_frame(self) -> bool:
        """
        checks if all routes are within the given timeframe

        returns:
            true if all stations are valid
        """

        # check time validity for every single route
        for route in self.routes:
            if not route.is_valid_time(self.time_frame):
                return False
        return True

    def less_than_max_routes(self) -> bool:
        """
        Checks if there are not more than the max number of routes

        returns:
            True if there are less routes than the max
        """
        if self.max_number_routes and \
                self.number_routes > self.max_number_routes:
            return False
        return True

    def all_connections_used(self) -> bool:
        """
        Checks if all connections are used.

        returns:
            True if all connections are used
        """
        if len(self.unused_connections) == 0:
            return True
        return False

    def is_valid_solution(self) -> bool:
        """
        Gives information about satisfaction of all constraints

        pre:
            constraint relaxation parameters (default: False)
            relax the three specific constraints if True

        returns:
            bool for overall constraint satisfaction
        """

        if (
                not self.relaxed_time_frame and
                not self.routes_valid_time_frame()
        ):
            return False

        if (
                not self.relaxed_max_routes and
                not self.less_than_max_routes()
        ):
            return False

        if (
            not self.relaxed_all_connections and
            not self.all_connections_used()
        ):
            return False
        return True
    
    def is_valid_solution_without_connection(self) -> bool:
        """
        Gives information about satisfaction of the two constraints

        pre:
            constraint relaxation parameters (default: False)
            relax the three specific constraints if True

        returns:
            bool for overall constraint satisfaction
        """

        if (
                not self.relaxed_time_frame and
                not self.routes_valid_time_frame()
        ):
            return False

        if (
                not self.relaxed_max_routes and
                not self.less_than_max_routes()
        ):
            return False

        return True

    def is_valid_solution_non_relaxed(self) -> bool:
        """
        Gives information about satisfaction of all constraints,
        without constraint relaxation

        returns:
            bool for overall constraint satisfaction
        """

        if not self.routes_valid_time_frame():
            return False
        if not self.less_than_max_routes():
            return False
        if not self.all_connections_used():
            return False
        return True

    def show(self) -> str:
        """
        Gives description of the current state.

        returns:
            description with:
                all routes with their connections
                score
        """
        result_string: str = "Routes:\n"
        for route in self.routes:
            result_string += f"- {route.name}:\n"
            for connection in route.route_connections:
                result_string += f"  - {connection}\n"
            result_string += f"Total minutes: {route.total_time}\n\n"
        result_string += f"Score: {self.calculate_score()}\n"
        if self.is_valid_solution_without_connection():
            result_string += "The current solution is valid."
        else:
            result_string += "The current solution is not valid."
        return result_string

    def show_sleeper_string(self) -> str:
        """
        Gives string that can 'awake' the current state at any later moment

        returns:
            string with:
            - quality score
            - fraction of used connections
            - number of routes
            - total distance driven
            - constraint relaxation values
                - all connections used
                - in time frame
                - max routes
            - routes
                - name
                - stations
            delimiters:
                1. \t
                2. ;
                3. :
                4: >
        """
        sleeper_string: str = ""

        # add quality score and parameters
        sleeper_string += \
            f"{self.score}\t" + \
            f"{self.fraction_used_connections}\t" + \
            f"{self.number_routes}\t" + \
            f"{self.total_minutes}\t"

        # add constraint relaxation values
        sleeper_string += \
            f"{self.relaxed_all_connections};" + \
            f"{self.relaxed_time_frame};" + \
            f"{self.relaxed_max_routes}\t"

        # add routes
        for r_index, route in enumerate(self.routes):
            sleeper_string += f"{route.name}:"
            for index, station in enumerate(route.route_stations):
                sleeper_string += station.name
                if index < len(route.route_stations) - 1:
                    sleeper_string += ">"
            if r_index < len(self.routes) - 1:
                sleeper_string += ";"

        return sleeper_string

    def get_standardized_sleeper_string(self) -> str:
        """
        gives a standardized sleeper string for archiving

        returns:
            string with all routes, sorted alphabetically
        """
        sleeper_list = []

        for route in self.routes:
            sleeper_route = "|"
            for station in route.route_stations:
                sleeper_route += station.name
            sleeper_list.append(sleeper_route)
        sleeper_list.sort()
        return str(sleeper_list)

    def awaken_state(self, sleeper_string: str):
        """
        'awakens' a certain state, using a sleeper string

        pre:
            sleeper_string is string with:
            - quality score
            - fraction of used connections
            - number of routes
            - total distance driven
            - constraint relaxation values
                - all connections used
                - in time frame
                - max routes
            - routes
                - name
                - stations
            the first delimiter is \t, the second is ;, the third is -

        post:
            updates:
                routes
                quality score
                score parameter attributes
                constraint relaxation value attributes
        """
        self.reset()
        sleeper_data: list[str] = sleeper_string.split("\t")

        # add quality score and quality score parameters
        self.score = float(sleeper_data[0])
        self.fraction_used_connections = float(sleeper_data[1])
        self.number_routes = int(sleeper_data[2])
        self.total_minutes = float(sleeper_data[3])

        # add constraint relaxation values
        constraint_relaxation_data: list = sleeper_data[4].split(";")
        self.relaxed_all_connections = bool(constraint_relaxation_data[0])
        self.relaxed_time_frame = bool(constraint_relaxation_data[1])
        self.relaxed_max_routes = bool(constraint_relaxation_data[2])

        # add routes
        routes_data: list = sleeper_data[5].split(";")
        for index, route_data in enumerate(routes_data):
            stations_list: list[str] = route_data.split(":")[1].split(">")
            connections_list: list['Connection'] = []
            for i in range(len(stations_list) - 1):
                for connection in self.connections:
                    station_1: 'Station' = connection.station_1
                    station_2: 'Station' = connection.station_2
                    if (
                        i + 1 < len(stations_list) and
                        (
                            (station_1.name == stations_list[i] and
                                station_2.name == stations_list[i + 1]) or
                            (station_2.name == stations_list[i] and
                                station_1.name == stations_list[i + 1])
                        )
                    ):
                        connections_list.append(connection)
            self.add_route(connections_list.pop(0))
            for connection in connections_list:
                self.routes[index].add_connection(connection)

    def show_csv_line(self, state_id: int, algorithm: str):
        """
        makes a line that can be added to data csv

        returns:
            list with:
            - state_id
            - algorithm
            - score
            - fraction_used_connections
            - number_routes
            - total_minutes
            - is_solution
            - sleeper_string
        """

        csv_line: list = [
            state_id,
            algorithm,
            self.calculate_score(),
            self.fraction_used_connections,
            self.number_routes,
            self.total_minutes,
            self.is_valid_solution_non_relaxed(),
            self.show_sleeper_string()]

        return csv_line

    def reset(self):
        """
        Resets the state.

        post:
            empties list of routes
            resets score and score parameters
            resets relaxations
        """

        # empty list of routes
        self.routes = []

        self.route_id_tracker = 1

        # reset relaxations
        self.relaxed_all_connections = False
        self.relaxed_max_routes = False
        self.relaxed_time_frame = False

        # reset score and score parameters
        self.score = 0.0
        self.fraction_used_connections = 0.0
        self.number_routes = 0
        self.total_minutes = 0

        # reset connection usage
        self.used_connections = []
        self.unused_connections = copy.copy(self.connections)
        for connection in self.connections:
            connection.used = 0

 