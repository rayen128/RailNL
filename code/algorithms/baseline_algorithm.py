from .algorithm import Algorithm
from ..classes.state import State
from ..classes.route import Route

import random
import copy


class Baseline_Algorithm(Algorithm):
    def __init__(self, state: object) -> None:
        super().__init__(state)
        

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
            # pick random connection and create route
            self.add_random_route()

            # variable to keep track of current route
            self.current_route_index = 0

            # add routes until time_frame is exceeded
            while self.state.routes[-1].is_valid_time(self.state.time_frame):

                # add random connection (and save if this was at the end or beginning)
                choice = self.add_random_connection(-1)

            # remove last-added connection
            self.delete_random_connection(-1, choice)
            # if choice == 'start':
            #     self.state.delete_start_connection_from_route(
            #         self.state.routes[-1])
            # elif choice == 'end':
            #     self.state.delete_end_connection_from_route(
            #         self.state.routes[-1])
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
            print(self.state.show())
            print(f"\n{self.current_route_index}")

            # add routes until time_frame is exceeded
            while self.state.routes[self.current_route_index].is_valid_time(self.state.time_frame):

                # add random connection (and save if this was at the end or beginning)
                choice = self.add_random_connection(self.current_route_index)

            # remove last-added connection
            self.delete_random_connection(self.current_route_index, choice)

            # set index to 1 higher
            self.current_route_index += 1

        self.return_score()
