# TODO: import state
import random


def random_algorithm_1(state: 'State') -> tuple(float, 'Route'):
    """
    pick random starting location/connection 
    then pick random follow-up 
    go on till all connections are picked
    save score
    """

    # pick random connection and create route
    state.add_route(random.choice(state.connections))

    # do loop until there is a valid solution
    while not state.is_valid_solution(relaxed_time_frame=True):
        # choose random new route
        new_connection = random.choice(
            state.routes[0].get_end_station().get_connections())

        state.routes[0].add_connection(new_connection)

    # save return variables
    score = state.calculate_score()
    route = state.routes[0]
    description = state.show()
    state.write_output("../../data/output_random_algorithm.csv")

    return score, route, description
