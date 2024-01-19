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

    def build_children(self, state):
        """
        TODO: docstring
        """
        # TODO: find a way to retrieve all possible values for a station
        values = None

        for value in values:
            new_state = copy.deepcopy(state)

            # TODO: vind a way to assign the value to the station
            self.states.append(new_state)

    def check_solution(self, new_state):
        new_value = new_state.calculate_score()
        old_value = self.best_value

        if new_value >= old_value:
            self.best_solution = new_state
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def run(self):
        while self.states:
            new_state = self.get_next_state()

            # TODO: find way to get next empty connection
            connection = new_state.something()

            if connection is not None:
                self.build_children(new_state, connection)
            else:
                self.check_solution(new_state)

        self.state = self.best_solution
