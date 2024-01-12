from station import Station
from connection import Connection


class Route():
    def __init__(self: 'Route', name: str) -> None:
        """
        initializes a Route class which maintains lists with information about a route

        post: 
            makes empty lists for the stations and the connections in a route
            sets the total time of a route at 0
        """
        self.name: str = name
        self.route_stations: list = []
        self.route_connections: list = []
        self.total_time: float = 0

    def get_start_station(self: 'Route') -> 'Station':
        """
        returns the first station in the station list

        pre: 
            list of stations is not empty.

        returns: 
            first station in the station list
        """
        assert self.route_stations != []

        return self.route_stations[0]

    def get_end_station(self: 'Route') -> 'Station':
        """
        returns the last station in the station list

        pre: 
            list of stations is not empty.

        returns: 
            last station in the station list
        """
        assert self.route_stations != []

        return self.route_stations[-1]

    def add_connection(self: 'Route', connection: 'Connection') -> None:
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

        # get start and end station
        start_station = self.get_start_station()
        end_station = self.get_end_station()

        # check if end station has the connection, if true add connection
        if end_station._has_connection(connection):
            self.route_connections.append(connection)
            self.add_station_end(
                self.get_other_station(connection, end_station))
            self.total_time += connection.distance
            
        # check if start station has the connection, if true add connection
        elif start_station._has_connection(connection):
            self.route_connections.insert(0, connection)
            self.add_station_start(self.get_other_station(
                connection, start_station))
            self.total_time += connection.distance

    def add_station_end(self: 'Route', station: 'Station') -> None:
        """
        adds station at the end of the list of stations

        pre: 
            station is a Station class
            self.route_stations is a list

        post: 
            the station object is added to the list of stations
        """
        self.route_stations.append(station)

    def add_station_start(self: 'Route', station: 'Station') -> None:
        """
        adds station object to beginning of station list

        pre: 
            station is a Station class
            self.route_stations is a list

        post: 
            the station object is added to the list of stations
        """
        self.route_connections.insert(0, station)

    def get_other_station(self: 'Route', connection: 'Connection', station: 'Station') -> 'Station':
        """
        returns the other station in a connection than the given station

        pre:
            connection is a Connection class which maintains two stations
            station is a Station class which maintains the name of the station

        returns:
            the other station in the connection than the given station if the given station is in connection
            none if the given station is not in connection
        """
       
        # TODO: deze code veranderen wanneer de stationsobjecten opgeslagen liggen in de connection class
        if station.name == connection.station_1:
            return connection.station_2

        elif station.name == connection.station_2:
            return connection.station_1
        
        return None

    def delete_connection_end(self: 'Route') -> None:
        """
        deletes the last connection
        
        pre: 
            the stations and connections lists are not empty
            the last station in stations list has the last connection in de connections list

        post: 
            deletes last connection from self.route_connections
            deletes last station from slef.route_stations
            substracts deleted connections distance from self.total_time
        """
        assert self.route_connections != [] and self.route_stations != [] and \
        self.total_time > 0 and self.route_stations[-1]._has_connection(self.route_connections[-1]),\
        "delete last connection is not possible"

        connection = self.route_connections.pop()
        self.route_stations.pop()
        self.total_time -= connection.distance

    def delete_connection_start(self: 'Route', connection: 'Connection') -> None:
        """
        deletes the first connection
        
        pre: 
            the stations and connections lists are not empty
            the first station in stations list has the first connection in de connections list

        post: 
            deletes first connection from self.route_connections
            deletes first station from slef.route_stations
            substracts deleted connections distance from self.total_time
        """
        assert self.route_connections != [] and self.route_stations != [] and \
        self.total_time > 0 and self.route_stations[0]._has_connection(self.route_connections[0]),\
        "delete first connection is not possible"

        connection = self.route_connections.pop(0)
        self.route_connections.pop(0)
        self.total_time -= connection.distance

    def is_station_in_route(self: 'Route', station: 'Station') -> bool:
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

    def is_connection_in_route(self: 'Route', connection: 'Connection') -> bool:
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
