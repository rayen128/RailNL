class Route():
    def __init__(self):
        """
        Post: 
            initiates Route object
        """
        pass

    def get_start_station(self):
        """
        pre: 
            list of stations is not empty.
        
        post: 
            gives first station in the station list
        """
        pass

    def get_end_station(self):
        """
        pre: 
            list of stations is not empty.
        
        post: 
            gives last station in the station list
        """
        pass

    def add_connection(self):
        """
        pre: 
            -
        
        post: 
            adds connection to begin or end of connections list 
            adds station to begin or end of stations list
        """
        pass

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