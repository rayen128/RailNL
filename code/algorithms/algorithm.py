from ..classes.state import State
import random
import copy
from typing import Union


class Algorithm():
    def __init__(self, state: 'State') -> None:
        self.state = state

    def add_random_route(self) -> None:
        """
        adds a random 1-length route to the state

        pre: 
            self.state is a state object
            self.state.connections contains connection objects

        post:
            added a 1-length route to self.state.routes
        """
        self.state.add_route(random.choice(self.state.connections))

    def create_random_state(self, number_of_connections: int = 1) -> None:
        """
        randomly generates a state with random 1-length routes (default=1)

        pre: 
            number_of_connections is an integer

        post:
            self.state.routes contains specified number of 1-length routes
        """
        for new_connection in range(number_of_connections):
            # pick random connection and create route
            self.add_random_route()

    def add_random_connection(self, route_index: int = 0, choice: Union[str, None] = None) -> str:
        """
        # TODO: doc-string
        """

        # determine choice if not prematurely done
        if choice == None:
            choice = random.choice(['start', 'end'])

        if choice == 'start':
            new_connection = random.choice(
                self.state.routes[route_index].get_start_station().get_connections())

        elif choice == 'end':
            new_connection = random.choice(
                self.state.routes[route_index].get_end_station().get_connections())

        self.state.routes[route_index].add_connection(new_connection)

        return choice

    def delete_random_connection(self, route_index: int = 0, choice: Union[str, None] = None) -> str:
        """
        # TODO: doc-string
        """
        # determine choice if not prematurely done
        if choice == None:
            choice = random.choice(['start', 'end'])

        if choice == 'start':
            random.choice(self.state.routes).delete_connection_start()

        elif choice == 'end':
            random.choice(self.state.routes).delete_connection_end

        return choice

    def delete_random_route(self) -> None:
        route = random.choice(self.state.routes)

        self.state.delete_route(route)

    def return_score(self) -> tuple[float, str]:
        """
        # TODO: doc-string
        """
        # save return variables
        score = self.state.calculate_score()
        description = self.state.show()

        return score, description

    def load_state(self, new_state: object) -> None:
        """
        # TODO: doc-string
        """
        self.state = new_state

    def read_sleeper_string(self, sleeper_string: str) -> None:
        """
        # TODO: doc-string
        """
        self.awaken_state(sleeper_string)
