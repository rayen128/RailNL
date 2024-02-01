import random
import csv
import copy
from ..algorithms.hill_climber import Hill_climber
from ..classes.state import State


class Advanced_7():
    """
    performs and saves the results of experiment 5 of the advanced RailNL case
    """

    def __init__(self, state: object, itterations: int) -> None:

        self.state = state

        self.itterations = itterations

        self.original_score: list[float] = []

        self.score_changes: dict[str: float] = {
            station.name: 0 for station in self.state.stations}

    def run(self):
        """
        run the algorithm
        """
        random.seed(42)
        print('loop 1')

        alg = Hill_climber(self.state)
        alg.valid_start_state = False

        for i in range(self.itterations):
            print(f"itteration {i}")
            station_to_eliminate = self.get_station(self.state)
            self.eliminate_station_fake(station_to_eliminate)
            alg.run(100, i, False)
            self.original_score.append(alg.state.score)

        random.seed(42)
        print('loop 2')

        for i in range(self.itterations):
            state_copy = copy.deepcopy(self.state)
            print(
                f"itteration {i}, aantal stations is: {len(self.state.stations)}")

            alg = Hill_climber(state_copy)
            alg.valid_start_state = False

            station_to_eliminate = self.get_station(state_copy)

            eliminated_station = self.eliminate_station(
                station_to_eliminate, state_copy)

            alg.run(100, i, False)
            score_difference = alg.state.score - self.original_score[i]
            self.score_changes[eliminated_station] += score_difference

        print(self.score_changes)
        self.write_to_csv()

    def eliminate_station(self, station_to_eliminate: object, state: object):
        """
        removes a station & all its connections
        """

        # remove station from state
        state.stations.remove(station_to_eliminate)

        # go over all connections and check they us the station to eliminate
        for connection in state.connections:
            if station_to_eliminate == connection.station_1:
                connection.station_2.connections.remove(connection)
                state.connections.remove(connection)

            elif station_to_eliminate == connection.station_2:
                connection.station_1.connections.remove(connection)
                state.connections.remove(connection)

        return station_to_eliminate.name

    def get_station(self, state: object):
        """
        returns random station from state
        """
        return random.choice(state.stations)

    def eliminate_station_fake(self, station_to_eliminate: object):
        """
        mimics the eliminate_station method
        """
        station_to_eliminate = station_to_eliminate

    def write_to_csv(self):
        pass


class Advanced_6(Advanced_7):
    """
    performs and saves the results of experiment 6 of the advanced RailNL case
    """

    def __init__(self, state: object, itterations: int) -> None:
        super().__init__(state, itterations)

    def get_station(self, state: 'State'):
        return self.state.stations[53]

    def write_to_csv(self):
        pass


class Advanced_5():
    """
    performs and saves the results of experiment 5 of the advanced RailNL case 
    """

    def __init__(self, state: object, itterations: int):

        self.state = state

        self.itterations: int = itterations

        self.original_score: list[float] = []

        self.score_changes = {
            i: [0, self.state.connections[i].station_1,
                self.state.connections[i].station_2]
            for i in range(len(self.state.connections))
        }

    def run(self) -> None:
        """
        run the advanced_5 experiment
        """

        # set seed
        random.seed(42)

        for i in range(self.itterations):
            self.move_tracks_fake()
            alg = Hill_climber(self.state)
            alg.valid_start_state = False
            alg.run(100, i)
            self.original_score.append(alg.state.score)

        # set same seed to ensure same 'randomness'
        random.seed(42)
        self.state.reset()

        print('loop 1 done')

        # replicate first section but now with moved tracks
        for i in range(self.itterations):
            tracks_used = self.move_tracks()
            alg = Hill_climber(self.state)
            alg.valid_start_state = False
            alg.run(100, i)
            score_difference = alg.state.score - self.original_score[i]
            self.save_scores(tracks_used, score_difference)

        self.write_to_csv()

    def save_scores(self, tracks_used: list[object], score_difference: float) -> None:
        """
        calculate the score difference between 
        """
        for connection_id in tracks_used:
            self.score_changes[connection_id][0] += score_difference

    def move_tracks_fake(self) -> None:
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

    def move_tracks(self) -> list[int]:
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

    def write_to_csv(self):
        with open('data/advanced/experiment_advanced_5.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Connection', 'From', 'To', 'value_change'])

            for key, value in self.score_changes.items():
                writer.writerow([key, value[1], value[2], value[0]])
