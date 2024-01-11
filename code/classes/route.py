class Route():
    def __init__(self):
        """Post: initiates Route object"""
        pass

    def get_start_station(self):
        """Pre: list of stations is not empty.
        Post: gives first station in the station list"""
        pass

    def get_end_station(self):
        """Pre: list of stations is not empty.
        Post: gives last station in the station list"""
        pass

    def add_connection(self):
        """Pre: -
        Post: adds connection to begin or end of connections list 
              adds station to begin or end of stations list"""
        pass

    def delete_connection(self):
        """Pre: given connection exists at begin or end of connections list
        Post: deletes given connection"""
        pass

    def is_valid_action(self):
        """Post: checks if an action is valid"""
        pass