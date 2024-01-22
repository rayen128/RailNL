from .algorithm import Algorithm
from ..classes.state import State
from ..classes.route import Route

import random
import copy

# FIXME: alg_3 loop tegen de volgende assert aan:
"""
Traceback (most recent call last):
  File "/mnt/c/Users/Rayen Oaf/Documents/Programming/Algoritmes & Heuristieken/AHRailNL/test.py", line 14, in <module>
    baseline_alg.baseline_algorithm_3()
  File "/mnt/c/Users/Rayen Oaf/Documents/Programming/Algoritmes & Heuristieken/AHRailNL/code/algorithms/baseline_algorithm.py", line 115, in baseline_algorithm_3    
    self.delete_random_connection(self.current_route_index, choice)
  File "/mnt/c/Users/Rayen Oaf/Documents/Programming/Algoritmes & Heuristieken/AHRailNL/code/algorithms/algorithm.py", line 95, in delete_random_connection
    random.choice(self.state.routes).delete_connection_start()
  File "/mnt/c/Users/Rayen Oaf/Documents/Programming/Algoritmes & Heuristieken/AHRailNL/code/classes/route.py", line 182, in delete_connection_start
    assert self.route_stations[0].has_connection(self.route_connections[0]), \
AssertionError: the first station in stations list has not the first connection in the connections list
"""


class Baseline_Algorithm(Algorithm):
    def __init__(self, state: object) -> None:
        super().__init__(state)
        self.current_route_index = 0

    def baseline_algorithm_1(self):
        """
        makes one route with a unlimited timeframe, but with all connections involved

        pre:
            self.state is a State object 

        post:
            makes one big route with all the connections

        returns:
            the score of the state
            the description of the state
        """

        # make sure state allows to go over the timeframe
        self.state.relaxed_time_frame = True

        self.create_random_state()

        # do loop until there is a valid solution (while max time_frame per route can be exceeded)
        while not self.state.is_valid_solution():
            # choose random new route
            self.add_random_connection(0)

        self.return_score()

    def baseline_algorithm_2(self):
        # FIXME: runs indefinitely, doesn't seem to know when to stop
        """
        makes unlimited routes with a limited timeframe until all are connections used

        pre:
            self.state is a State object 

        post:
            makes several routes with all the connections

        returns:
            the score of the state
            the made route
            the description of the state  
        """
        # make sure state allows to go over the max amount of routes
        self.state.relaxed_max_routes = True

        # do loop until there is a valid solution (while max routes can be exceeded)
        while not self.state.is_valid_solution():
            print(self.state.show())
            # pick random connection and create route
            self.add_random_route()

            # variable to keep track of current route
            self.current_route_index = 0

            # add routes until time_frame is exceeded
            while self.state.routes[self.current_route_index].is_valid_time(self.state.time_frame):

                # add random connection (and save if this was at the end or beginning)
                choice = self.add_random_connection(self.current_route_index)

            # remove last-added connection
            self.delete_random_connection(self.current_route_index, choice)
            # self.state.routes[self.current_route_index].delete_random_connection(choice)
            self.current_route_index += 1

        self.return_score()

    def baseline_algorithm_3(self):
        """
        makes 7 route(s) with with the time_frame constraint but not all the connections necessary

        pre:
            self.state is a State object 

        post:
            makes route(s)

        returns:
            the score of the state
            the made route
            the description of the state
        """
        # variable to keep track of current route
        self.current_route_index = 0

        # loop until 7 routes routes are created
        while len(self.state.routes) < 7:

            # create a new route
            self.add_random_route()

            # add routes until time_frame is exceeded
            while self.state.routes[self.current_route_index].is_valid_time(self.state.time_frame):

                # add random connection (and save if this was at the end or beginning)
                choice = self.add_random_connection(self.current_route_index)

            # remove last-added connection
            self.delete_random_connection(self.current_route_index, choice)

            # set index to 1 higher
            self.current_route_index += 1

        self.return_score()


def random_algorithm_1(state: 'State') -> tuple[float, 'Route', str]:
    """
    makes one route with a unlimited timeframe, but with all connections involved

    pre:
        state is a State object 

    post:
        makes one big route with all the connections

    returns:
        the score of the state
        the made route
        the description of the state
    """
    # make sure state allows to go over the timeframe
    state.relaxed_time_frame = True

    # pick random connection and create route
    state.add_route(random.choice(state.connections))

    # do loop until there is a valid solution (while max time_frame per route can be exceeded)
    while not state.is_valid_solution():
        # choose random new route
        new_connection = random.choice(
            state.routes[0].get_end_station().get_connections())

        state.routes[0].add_connection(new_connection)

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()

    return score, route, description


def random_algorithm_2(state: 'State') -> tuple[float, 'Route', str]:
    """
    makes unlimited routes with a limited timeframe until all are connections used

    pre:
        state is a State object 

    post:
        makes several routes with all the connections

    returns:
        the score of the state
        the made route
        the description of the state  
    """
    # make sure state allows to go over the max amount of routes
    state.relaxed_max_routes = True

    # variable to keep track of current route
    current_route_index = 0

    # do loop until there is a valid solution (while max routes can be exceeded)
    while not state.is_valid_solution():

        # pick random connection and create route
        state.add_route(random.choice(state.connections))

        # add routes until time_frame is exceeded
        while state.routes[current_route_index].is_valid_time(state.time_frame):

            # choose random new route
            new_connection = random.choice(
                state.routes[current_route_index].get_end_station().get_connections())

            state.routes[current_route_index].add_connection(new_connection)

        state.routes[current_route_index].delete_connection_end()
        current_route_index += 1

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()

    return score, route, description


def random_algorithm_3(state: 'State') -> tuple[float, 'Route', str]:
    """
    makes 7 route(s) with with the time_frame constraint but not all the connections necessary

    pre:
        state is a State object 

    post:
        makes route(s)

    returns:
        the score of the state
        the made route
        the description of the state
    """

    # variable to keep track of current route
    current_route_index = 0

    # loop until 7 routes routes are created
    while len(state.routes) < 7:

        # pick random connection and create route
        state.add_route(random.choice(state.connections))

        # print(current_route_index)

        # add connections to route until time_frame is exceeded
        while state.routes[current_route_index].is_valid_time(state.time_frame):

            # choose random new route
            new_connection = random.choice(
                state.routes[current_route_index].get_end_station().get_connections())

            state.routes[current_route_index].add_connection(new_connection)

        state.routes[current_route_index].delete_connection_end()
        current_route_index += 1

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()

    return score, route, description


def random_algorithm_4(state: 'State') -> tuple[float, 'Route', str]:

    connection_list = copy.copy(state.connections)

    while connection_list:
        # print(state.show())
        random_connection = random.choice(connection_list)
        # print(random_connection)
        if state.routes:
            shuffled_routes = random.sample(state.routes, len(state.routes))
        else:
            shuffled_routes = []
        connection_added = False
        for route in shuffled_routes:
            if route.add_connection(random_connection):
                connection_added = True
                break
        if not connection_added:
            if not state.add_route(random_connection):
                print(shuffled_routes)
                route_deleted = random.choice(shuffled_routes)
                connection_list += route_deleted.route_connections
                state.delete_route(route_deleted)
                state.add_route(random_connection)
        connection_list.remove(random_connection)

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()

    return score, route, description
