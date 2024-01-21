from algorithm import Algorithm

class Hill_climber(Algorithm):
    def __init__(self, state: object, valid_states: bool):
        super().__init__(state)
        self.start_state = self.create_valid_state()
        self.state_list = []

    def create_valid_state(self):
        route_counter = 0
        while not self.state.is_valid_solution():
            if self.state.number_routes < self.state.max_number_routes:
                self.add_random_route()
            else:
                self.state.delete_route(self.state.routes[route_counter - 1])
                self.add_random_route()
                print(self.state.number_routes)
                print(self.state.show())
                route_counter -= 1
            while self.state.routes[route_counter].is_valid_time(self.state.time_frame):
                connection_added = False
                for connection in self.state.connections:
                    if connection.used == 0:
                        connection_added = state.routes[route_counter].add_connection(connection)
                if not connection_added: 
                    for connection in self.state.connections:
                        state.routes[route_counter].add_connection(connection)
            route_counter += 1
            print(self.state.show())

if __name__ == "__main__":
    from sys import argv, path
    path.append("../classes")
    from state import State

    state = State('../../data/stations_holland.csv', '../../data/routes_holland.csv', 7, 120)
    hillclimber = Hill_climber(state, True)
    
    print(hillclimber.current_state.show())





    
