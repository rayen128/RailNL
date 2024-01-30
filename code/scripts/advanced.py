import random
from ..algorithms.hill_climber import *


class Advanced_7():
    """
    Test voor uitval van andere stations hoe groot de impact is op je beste lijnvoering.
    """

    def __init__(self, state: object) -> None:

        self.state = state

        self.itterations: int = 25

        self.original_score: list[float] = []

        self.score_changes: dict[str: float] = {
            station.name: 0 for station in self.state.stations}

    def run(self):
        """
        run
        """
        random.seed(42)

        for i in self.itterations:
            self.eliminate_station_fake()
            alg = Hill_climber(self.state)
            alg.run(100, i)
            self.original_score.append(alg.state.score)

        random.seed(42)

        for i in self.itterations:
            eliminated_station = self.eliminate_station()
            alg = Hill_climber(self.state)
            alg.run(100, i)
            score_difference = alg.state.score - self.original_score[i]
            self.score_changes[eliminated_station] += score_difference

    def eliminate_station(self):
        """
        removes a station & all its connections
        """
        station_to_eliminate = random.choice(self.state.stations)

        # remove station from state
        self.state.remove(station_to_eliminate)

        # go over all connections and check they us the station to eliminate
        for connection in self.state.connections:
            if station_to_eliminate == connection.station_1:
                connection.station_2.remove(connection)
                self.state.connections.remove(connection)

            elif station_to_eliminate == connection.station_2:
                connection.station_1.remove(connection)
                self.state.connections.remove(connection)

        return station_to_eliminate.name

    def eliminate_station_fake(self):
        """
        mimics the eliminate_station method
        """
        station_to_eliminate = random.choice(self.state.stations)


class Advanced_5():
    """
    Verleg drie random sporen en run je algoritmen nog een keer.
    Vind je nu betere of slechtere waarden voor de doelfunctie? 
    Doe dit een paar keer, en probeer erachter te komen welke sporen de grootste invloed hebben op de doelfunctie. 
    """

    def __init__(self, state: object):

        self.state = state

        self.itterations: int = 25

        self.original_score: list[float] = []

        self.score_changes: dict[int: float] = {
            key: 0 for key in range(0, len(self.state.connections))}

    def run(self):
        """
        run the advanced_5 experiment
        """

        # set seed
        random.seed(42)

        for i in range(self.itterations):
            self.move_tracks_fake()
            alg = Hill_climber(self.state)
            alg.run(100, i)
            self.original_score.append(alg.state.score)

        # set same seed to ensure same 'randomness'
        random.seed(42)

        # replicate first section but now with moved tracks
        for i in range(self.itterations):
            tracks_used = self.move_tracks()
            alg = Hill_climber(self.state)
            alg.run(100, i)
            score_difference = alg.state.score - self.original_score[i]
            self.save_scores(tracks_used, score_difference)

    def save_scores(self, tracks_used, score_difference):
        """
        calculate the score difference between 
        """
        for connection_id in tracks_used:
            self.score_changes[connection_id] += score_difference

    def move_tracks_fake(self):
        """
        does nothing but replicating the 'decisions' of the real move_tracks
        """
        for i in range(3):
            connection = random.choice(self.state.connections)

            # create new_end_station variable
            old_end_station = connection.station_2
            new_end_station = connection.station_2

            # pick new station until it's different than the current 1
            while connection.station_2 == new_end_station:
                new_end_station = random.choice(self.state.stations)

    def move_tracks(self):
        """
        move three random tracks and change the state accordingly
        """
        tracks_used = []

        # move track 3 times
        for i in range(3):
            # pick a random connection
            connection = random.choice(self.state.connections)

            # save which tracks are used
            tracks_used.append(connection.id)

            print(f"id= {connection.id}")

            # create new_end_station variable
            old_end_station = connection.station_2
            new_end_station = connection.station_2

            # pick new station until it's different than the current 1
            while connection.station_2 == new_end_station:
                new_end_station = random.choice(self.state.stations)

            # remove connection from the old end station
            old_end_station.connections.remove(connection)

            # add connection to the new end station
            new_end_station.connections.append(connection)

            # change end station of the connection
            connection.station_2 = new_end_station

        return tracks_used
