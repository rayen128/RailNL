import copy


class DepthFirst:
    """
    TODO: docstring
    """

    def __init__(self, state):
        self.state = copy.deepcopy(state)

        self.states = [copy.deepcopy(state)]

        self.best_solution = None
        self.best_value = 0

    def get_next_state(self):
        """
        TODO: docstring
        """
        return self.states.pop()

    def build_children(self, state, route):
        """
        TODO: docstring
        """
        values = route.get_end_station().get_connections()
        values += route.get_start_station().get_connections()
        print(f"Values: {values}")

        for value in values:
            new_state = copy.deepcopy(state)

            new_state.routes[-1].add_connection(value)

            if state.calculate_score() != new_state.calculate_score():
                self.states.append(new_state)

    def check_solution(self, new_state):
        new_value = new_state.calculate_score()
        old_value = self.best_value

        if new_value >= old_value:
            self.best_solution = new_state
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def get_smallest_connection(self, state, route) -> int:
        # get all possible connections
        connections = route.get_end_station().get_connections()
        print([connection for connection in connections])
        connections += route.get_start_station().get_connections()
        print([connection for connection in connections])

        # code provided by ChatGPT
        def key_function(obj): return obj.distance

        # Use the min function with the key function to find the connection with the lowest distance value
        min_connection = min(connections, key=key_function)

        return min_connection.distance

    def get_route(self, state):
        if not state.routes:
            state.add_route(state.unused_connections[0])
        route_to_return = state.routes[-1]

        if not route_to_return.route_connections or (state.time_frame - route_to_return.total_time < self.get_smallest_connection(state, route_to_return)):
            return route_to_return
        else:
            state.add_route(state.unused_connections[0])

    def run(self):
        while self.states:
            new_state = self.get_next_state()

            route = self.get_route(new_state)

            if route is not None:
                self.build_children(new_state, route)
            else:
                self.check_solution(new_state)

        self.state = self.best_solution
