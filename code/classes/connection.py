class Connection():

    def __init__(self, station_1: str, station_2: str, distance: float) -> None:
        """
        initializes Connection-class

        pre: 
            both station_1 and station_2 are strings
            distance is a float

        post:
            Connection-object       
        """

        assert isinstance(station_1, str) and isinstance(
            station_2, str), 'First (station_1) and second argument (station_2) should both be strings'

        self.station_1 = station_1
        self.station_2 = station_2
        self.distance = distance
