from .algorithm import Algorithm
from sys import path
path.append("../classes")
from state import State

import random
import copy
from sys import path


class Hill_climber(Algorithm):
    def __init__(self, state: object, valid_start_state: bool = True) -> None:
        """
        initializes the hillclimber with a starting state

        pre: 
            the given state is a object

        post: 
            creates a start state for self.state and copies that to self.current_state
        """

        super().__init__(state)

        self.valid_start_state = valid_start_state

        self.current_state = copy.deepcopy(self.state)

    def create_state(self) -> None:
        """
        creates a start state

        pre:
            self.valid_start_state is a boolean

        post:
            a random or a valid start state is created 
        """
        if self.valid_start_state:
            self.create_valid_state()
        else:
            self.create_random_state()

    def create_valid_state(self) -> None:
        """
        creates for self.state a start-state that is valid 

        pre:
            self.state doesn't consist of any routes
            there aren't any used connections in self.state

        post:
            self.state is now valid solved state
        """
        assert not self.state.routes, "there are already routes in this state"
        assert not self.state.used_connections, "there are used connections"

        self.current_route_index = 0
        # add routes until state is valid
        while not self.state.is_valid_solution():
            # add route if the max amount is not reached
            if self.state.number_routes < self.state.max_number_routes:
                self.add_random_route()
            # if max is reached delete random route and add route after that
            else:
                self.delete_random_route()
                self.add_random_route()
                self.current_route_index -= 1

            # add connections until timeframe is reached
            while self.state.routes[self.current_route_index].is_valid_time(self.state.time_frame):
                connection_added = False
                # try to add unused connections
                for connection in self.state.unused_connections:
                    if self.state.add_connection_to_route(self.state.routes[self.current_route_index], connection):
                        connection_added = True
                        break
                if not connection_added:
                    for connection in self.state.connections:
                        if self.state.add_connection_to_route(self.state.routes[self.current_route_index], connection):
                            break
            # delete connections above timeframe
            while not self.state.routes[self.current_route_index].is_valid_time(self.state.time_frame):
                self.state.delete_end_connection_from_route(
                    self.state.routes[self.current_route_index])

            self.current_route_index += 1

    def make_change_heavy(self) -> None:
        """
        makes one change in the state

        pre:
            self.state is an already solved state

        post:
            a route is added or deleted or a connection is added or deleted in self.state
        """
        random_number = random.randint(0, 100)
        # if connections can not be added but routes can
        if not self.choose_route_to_add_connection() and \
                self.state.number_routes < self.state.max_number_routes:
            if random_number <= 45:
                self.delete_random_connection()
            elif random_number >= 46 and random_number <= 80:
                self.add_random_route()
            elif self.state.number_routes > 1:
                self.delete_random_route()

        # if both routes and connections can not be added
        elif not self.choose_route_to_add_connection() and \
                self.state.number_routes >= self.state.max_number_routes:
            if random_number <= 65:
                self.delete_random_connection()
            elif self.state.number_routes > 1:
                self.delete_random_route()

        # if routes and connections can be added
        elif self.state.number_routes < self.state.max_number_routes:
            if random_number <= 35:
                self.delete_random_connection()
            elif random_number >= 36 and random_number <= 60:
                route_number = self.choose_route_to_add_connection()
                self.add_random_connection(route_number)
            elif random_number >= 61 and random_number <= 85:
                self.add_random_route()
            elif self.state.number_routes > 1:
                self.delete_random_route()

        # if connections can be added but routes not
        elif self.state.number_routes >= self.state.max_number_routes:
            if random_number <= 45:
                self.delete_random_connection()
            elif random_number >= 46 and random_number <= 75:
                route_number = self.choose_route_to_add_connection()
                self.add_random_connection(route_number)
            elif self.state.number_routes > 1:
                self.delete_random_route()

    def make_change_light(self) -> None:
        """
        makes one change in the state

        pre:
            self.state is an already solved state

        post:
            a route is added or deleted or a connection is added or deleted in self.state
        """
        random_number = random.randint(0, 100)
        if not self.choose_route_to_add_connection():
            self.delete_random_connection()

        else:
            if random_number <= 40:
                route_number = self.choose_route_to_add_connection()
                self.add_random_connection(route_number)
            else:
                self.delete_random_connection()

    def get_score_state(self, state: 'State') -> float:
        """
        get the score for a state with negative points for a non-valid state

        pre: 
            self.state has a score 

        returns:
            the calculated score
        """
        score = state.calculate_score()

        return score

    def compare_scores_state(self) -> None:
        """
        compares the scores from the current state and the changed state

        pre:
            both states has scores

        post:
            both current state as state are now the state with the highest score
        """
        # get scores for both states
        score_new_state = self.get_score_state(self.state)
        score_old_state = self.get_score_state(self.current_state)

        # compare scores and change states
        if score_new_state >= score_old_state:
            self.current_state = copy.deepcopy(self.state)
        else:
            self.state = copy.deepcopy(self.current_state)

    def choose_route_to_add_connection(self) -> int:
        """
        makes a list with routes who will be able to add a connection to

        pre:
            state has routes filled with at least one connection

        returns:
            a random route from the list with routes able to add a connection
        """
        # add routes with enough time left to add connections to list
        routes_able_to_add_connection = []
        for index in range(self.state.number_routes - 1):
            if self.state.routes[index].total_time <= self.state.time_frame - 20:
                routes_able_to_add_connection.append(index)
        # return none if there are no routes
        if routes_able_to_add_connection == []:
            return None

        random_route = random.choice(routes_able_to_add_connection)

        return random_route

    def run(self, iterations: int, algorithm_id: int, change_light: bool = True) -> list[float]:
        """
        runs the hillclimber

        pre:
            iterations is a integer
        returns:
            list of scores of all iterations
        """
        self.state.reset()
        self.create_state()
        self.current_state = copy.deepcopy(self.state)

        hillclimber_score_list = []
        for _ in range(iterations):
            if not change_light:
                self.make_change_heavy()
            else:
                self.make_change_light()
            self.compare_scores_state()
            hillclimber_score_list.append(self.current_state.calculate_score())

        return hillclimber_score_list


class Hill_climber_restart(Hill_climber):
    def __init__(self, state: 'State', restart_number: int, valid_start_state: bool = True) -> None:
        super().__init__(state)
        self.restart = restart_number
        self.restart_counter = 0
        self.valid_start_state = valid_start_state

    def compare_scores_state_restart(self) -> None:
        """
        compares the scores from the current state and the changed state

        pre:
            both states has scores

        post:
            both current state as state are now the state with the highest score
        """
        # get scores for both states
        score_new_state = self.get_score_state(self.state)
        score_old_state = self.get_score_state(self.current_state)

        # compare scores and change states
        if score_new_state >= score_old_state:
            self.current_state = copy.deepcopy(self.state)
            self.restart_counter = 0
        else:
            self.state = copy.deepcopy(self.current_state)
            self.restart_counter += 1

    def run(self, iterations: int, algorithm_id: int, change_light: bool = True) -> tuple[float, 'State', list]:
        """
        runs the hillclimber

        pre:
            iterations is a integer

        returns:
            best score
            sleeper string of the state with best score
            list of all scores
        """

        self.state.reset()
        self.create_state()
        self.current_state = copy.deepcopy(self.state)
        self.restart_counter = 0

        best_score = 0
        best_state = copy.deepcopy(self.state)

        hillclimber_score_list = []
        for _ in range(iterations):
            if not change_light:
                self.make_change_heavy()
            else:
                self.make_change_light()
            self.compare_scores_state_restart()
            if self.restart_counter >= self.restart:
                self.state.reset()
                self.create_state()
                self.current_state = copy.deepcopy(self.state)
                self.restart_counter = 0

            new_score = self.current_state.calculate_score()

            # check for new best score
            if new_score > best_score:
                best_score = new_score
                best_state = copy.deepcopy(self.current_state)

            hillclimber_score_list.append(new_score)

        return best_score, best_state, hillclimber_score_list
