class Connection():

    def __init__(self: 'Connection', station_1: object, station_2: object, distance: float) -> None:
        """
        initializes Connection-class

        pre: 
            both station_1 and station_2 are strings
            distance is a float

        post:
            Connection-object is created
        """

        assert isinstance(
            station_1, object), 'station_1 should be a station object'

        assert isinstance(
            station_2, object), 'station_2 should be a station object'

        self.station_1 = station_1
        self.station_2 = station_2
        self.distance = distance
        self.used = 0

    def __str__(self):
        return f"Connection from {self.station_1} to {self.station_2}"
