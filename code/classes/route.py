from station import Station
from connection import Connection


class Route():
    def __init__(self) -> None:
        """
        initializes a Route class which maintains lists with information about a route

        post: 
            makes empty lists for the stations and the connections in a route
            sets the total time of a route at 0
        """
        self.route_stations: list = []
        self.route_connections: list = []
        self.total_time: int = 0

    def get_start_station(self) -> object:
        """
        returns the first station in the station list

        pre: 
            list of stations is not empty.

        returns: 
            first station in the station list
        """
        assert self.route_stations != []

        return self.route_stations[0]

    def get_end_station(self) -> object:
        """
        returns the last station in the station list

        pre: 
            list of stations is not empty.

        returns: 
            last station in the station list
        """
        assert self.route_stations != []

        return self.route_stations[-1]

    def add_connection(self, connection: object) -> None:
        """
        adds connection to route if the end station or start station 
            has this connection
        if both the end station and the start station has the 
            given connection, the connection is only added at the end of the list

        pre: 
            connection is a valid Connection object

        post: 
            adds connection to begin or end of connections list 
            adds station to begin or end of stations list
            adds the connection distance to the total route time
        """
        #
        start_station = self.get_start_station()
        end_station = self.get_end_station()

        if end_station.has_connection(connection):
            self.route_connections.append(connection)
            self.add_station_end(
                self.get_other_station(connection, end_station))
            self.total_time += connection.distance

        elif start_station.has_connection(connection):
            self.route_connections.insert(0, connection)
            self.add_station_start(self.get_other_station(
                connection, start_station))
            self.total_time += connection.distance

    def add_station_end(self, station: object) -> None:
        self.route_stations.append(station)

    def add_station_start(self, station: object):
        self.route_connections.insert(0, station)

    def get_other_station(self, connection: object, station: object):

        # TODO: deze code veranderen wanneer de stationsobjecten opgeslagen liggen in de connection class
        if station.name == connection.station_1:
            return connection.station_2

        elif station.name == connection.station_2:
            return connection.station_1

    def delete_connection_end(self, connection: object):
        """
        pre: 
            given connection exists at begin or end of connections list

        post: 
            deletes given connection
        """
        connection = self.route_connections.pop()
        self.route_connections.pop()
        self.total_time -= connection.distance

    def delete_connection_start(self, connection: object):
        """
        pre: 
            given connection exists at begin or end of connections list

        post: 
            deletes given connection
        """
        connection = self.route_connections.pop(0)
        self.route_connections.pop(0)
        self.total_time -= connection.distance

    def is_station_in_route(self, station: object) -> bool:
        """
        checks if station is already in this route

        pre: 
            station is a valid object

        returns:
            true if station is already in route, false otherwise
        """
        if station in self.route_stations:
            return True

        return False

    def is_connection_in_route(self, connection: object) -> bool:
        """
        checks if connection is already in this route

        pre: 
            connection is a valid object

        returns:
            true if connection is already in route, false otherwise
        """
        if connection in self.route_connections:
            return True

        return False
