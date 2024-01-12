# from ..classes.state import state
import random


def random_algorithm_1(state: 'State') -> tuple[float, 'Route', str]:
    """
    # TODO: doc-string
    """

    # pick random connection and create route
    state.add_route(random.choice(state.connections))

    # do loop until there is a valid solution (while max time_frame per route can be exceeded)
    while not state.is_valid_solution(relaxed_time_frame=True):
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
    # TODO: doc-string    
    """

    # do loop until there is a valid solution (while max routes can be exceeded)
    while not state.is_valid_solution(relaxed_max_routes=True):

        # pick random connection and create route
        state.add_route(random.choice(state.connections))

        index = (state.number_routes - 1)

        # add routes until time_frame is exceeded
        while state.routes[index].is_valid_time(state.time_frame):

            # choose random new route
            new_connection = random.choice(
                state.routes[index].get_end_station().get_connections())

            state.routes[index].add_connection(new_connection)

        state.routes[index].delete_connection_end()

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()

    return score, route, description


def random_algorithm_3(state: 'State') -> tuple[float, 'Route', str]:
    """
    # TODO: doc-string    
    """

    # variable to keep track of current route
    current_route_index = 0

    # do loop until there is a valid solution (while max routes can be exceeded)
    while not state.is_valid_solution(relaxed_all_connections=False):

        # pick random connection and create route
        state.add_route(random.choice(state.connections))

        # add routes until time_frame is exceeded
        while route.is_valid_time():

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
