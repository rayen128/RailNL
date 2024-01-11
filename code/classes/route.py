class Route():
    def __init__(self):
        """
        post: 
            initiates Route object
        """
        self.route_stations: list = []
        self.route_connections: list = []


    def get_start_station(self):
        """
        pre: 
            list of stations is not empty.
        
        post: 
            gives first station in the station list
        """
        return self.route_stations[0]


    def get_end_station(self):
        """
        pre: 
            list of stations is not empty.
        
        post: 
            gives last station in the station list
        """
        return self.route_stations[-1]


    def add_connection(self, connection: object):
        """
        pre: 
            -
        
        post: 
            adds connection to begin or end of connections list 
            adds station to begin or end of stations list
        """
        start_station =
        
        self.route_connections.append(connection)


    def delete_connection(self):
        """
        pre: 
            given connection exists at begin or end of connections list
        post: 
            deletes given connection
        """
        pass

    def is_valid_action(self):
        """
        post: 
            checks if an action is valid
        """
        pass