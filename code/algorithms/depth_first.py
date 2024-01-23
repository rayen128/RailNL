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

        self.archive: set[str] = set()

    def get_next_state(self):
        """
        TODO: docstring
        """
        return self.states.pop()

    def get_connection_dict(self, connection: 'Connection') -> dict:
        return_dict: dict = {}
        return_dict['station_1'] = connection.station_1
        return_dict['station_2'] = connection.station_2

    def build_children(self, state, route):
        """
        TODO: docstring
        """
        print("Entering new build_children...")
        # get values to add to new states
        print(route)
        values = route.get_end_station().get_connections()
        # for connection in route.get_start_station().get_connections():
        #     if connection not in values:
        #         values.append(connection)

        # print(values)

        for value in values:
            # print(f"Value: {value}")
            # get something to let the value compare
            value_dict = self.get_connection_dict(value)

            new_state = copy.deepcopy(state)

            for connection in new_state.connections:

                # get something to compare the value with
                connection_dict = self.get_connection_dict(connection)
                if connection_dict == value_dict:
                    connection_to_add = connection
                    break

            new_state.add_connection_to_route(
                new_state.routes[-1], connection_to_add)

            if state.calculate_score() != new_state.calculate_score():
                # print(
                #     f"other score found. Old score: {state.calculate_score()}. New score: {new_state.calculate_score()}")
                std_sleeper_string = new_state.get_standardized_sleeper_string()
                if std_sleeper_string not in self.archive:
                    self.archive.add(std_sleeper_string)
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
        connections += route.get_start_station().get_connections()

        def key_function(connection):
            return connection.distance

        # Use the min function with the key function to find the connection with the lowest distance value
        min_connection = min(connections, key=key_function)

        return min_connection.distance

    def get_route(self, state):
        if not state.routes:
            state.add_route(state.unused_connections[0])
        route_to_return = state.routes[-1]

        print(self.get_smallest_connection(state, route_to_return))

        if state.time_frame - route_to_return.total_time > self.get_smallest_connection(state, route_to_return):
            return route_to_return
        else:
            if state.unused_connections:
                state.add_route(state.unused_connections[0])
                return state.routes[-1]

    def run(self):
        while self.states:
            print(f"stack length: {len(self.states)}")
            new_state = self.get_next_state()

            route = self.get_route(new_state)

            if route is not None:
                self.build_children(new_state, route)
            else:
                self.check_solution(new_state)

        self.state = self.best_solution
        print(self.best_solution.show())
