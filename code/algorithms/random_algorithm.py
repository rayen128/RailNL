# from ..classes.state import state
import random
import copy


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
    while len(state.routes) <= 7:

        # pick random connection and create route
        state.add_route(random.choice(state.connections))

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
        random_connection = random.choice(connection_list)
        shuffled_routes = random.shuffle(state.routes)
        connection_added = False
        for route in shuffled_routes:
            if route.add_connection(random_connection):
                connection_added = True
                break
        if not connection_added:
            if not state.add_route(random_connection):
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
