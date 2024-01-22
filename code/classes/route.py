from station import Station
from connection import Connection


class Route():
    def __init__(self: 'Route', name: str, connection: 'Connection') -> None:
        """
        initializes a Route class which maintains lists with information about a route

        pre: 
            connection is a Connection object with a station_1 and a station_2
            name is a string

        post: 
            makes empty lists for the stations and the connections in a route
            sets the total time of a route at 0
        """
        assert connection.station_1 != None and connection.station_2 != None, "connections has no stations"
        assert isinstance(name, str), "name is no string"

        self.name: str = name
        self.route_stations: list['Station'] = [
            connection.station_1, connection.station_2]
        connection.used += 1
        self.route_connections: list['Connection'] = [connection]
        self.total_time: float = 0

    def __str__(self):
        return f"Route with name {self.name}"

    def get_start_station(self: 'Route') -> 'Station':
        """
        returns the first station in the station list

        pre: 
            list of stations has two or more stations

        returns: 
            first station in the station list
        """
        assert len(self.route_stations) >= 2, "not enough stations in list"

        return self.route_stations[0]

    def get_end_station(self: 'Route') -> 'Station':
        """
        returns the last station in the station list

        pre: 
            list of stations has two or more stations

        returns: 
            last station in the station list
        """
        assert len(self.route_stations) >= 2, "not enough stations in list"

        return self.route_stations[-1]

    def add_connection(self: 'Route', connection: 'Connection') -> bool:
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
        if end_station.has_connection(connection):
            self.route_connections.append(connection)
            self.add_station_end(
                self.get_other_station(connection, end_station))
            self.total_time += connection.distance
            connection.used += 1
            return True

        # check if start station has the connection, if true add connection
        elif start_station.has_connection(connection):
            self.route_connections.insert(0, connection)
            self.add_station_start(self.get_other_station(
                connection, start_station))
            self.total_time += connection.distance
            connection.used += 1
            return True

        return False

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
        self.route_stations.insert(0, station)

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
        if station == connection.station_1:
            return connection.station_2

        elif station == connection.station_2:
            return connection.station_1

        return False

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
        
        assert self.route_stations[-1].has_connection(self.route_connections[-1]), \
            "the last station in stations list has not the last connection in the connections list"

        if len(self.route_connections) > 1:
            connection = self.route_connections.pop()
            self.route_stations.pop()
            self.total_time -= connection.distance
            connection.used -= 1
            return True
        return False

    def delete_connection_start(self: 'Route') -> None:
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
        assert self.route_stations[0].has_connection(self.route_connections[0]), \
            "the first station in stations list has not the first connection in the connections list"
        
        if len(self.route_connections) > 1:
            connection = self.route_connections.pop(0)
            self.route_stations.pop(0)
            self.total_time -= connection.distance
            connection.used -= 1
            return True
        return False

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

    def is_valid_time(self: 'Route', time_frame: int) -> bool:
        """
        checks if the time of the route is under the time frame and 

        pre:
            timeframe is integer

        returns:
            true if route is valid false if route is invalid
        """
        assert isinstance(time_frame, int), "timeframe is not a integer"

        if self.total_time >= time_frame:
            return False

        return True

    def is_valid_lists(self: 'Route') -> bool:
        """
        checks if consecutive stations has a connection

        returns: 
            false if stations or connections list is invalid
            true if stations and connections lists are valid
        """
        for number in range(len(self.route_stations) - 1):
            if not self.route_stations[number].has_connection(self.route_connections[number]):
                return False
            if self.route_stations[number].get_other_station(self.route_connections[number]) != self.route_stations[number + 1]:
                return False

        return True
