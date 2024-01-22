from algorithm import Algorithm
import random

class Hill_climber(Algorithm):
    def __init__(self, state: object, valid_start_state: bool = True):
        super().__init__(state)
        self.valid_start_state = valid_start_state
        self.state_list = []

        self.create_state()

    def create_state(self):
        if self.valid_start_state:
            self.create_valid_state()
        else:
            self.create_random_state()
            
    def create_valid_state(self):
        assert not self.state.routes, "there are already routes in this state"
        assert not self.state.used_connections, "there are used connections"
        
        route_counter = 0
        while not self.state.is_valid_solution():
            if self.state.number_routes < self.state.max_number_routes:
                self.add_random_route()
            else:
                random_number = random.randint(0, (self.state.max_number_routes -1))
                self.state.delete_route(self.state.routes[random_number])
                self.add_random_route()
                route_counter -= 1
            while self.state.routes[route_counter].is_valid_time(self.state.time_frame):
                connection_added = False
                for connection in self.state.unused_connections:
                    if self.state.add_connection_to_route(self.state.routes[route_counter], connection):
                        connection_added = True
                        break  
                if not connection_added: 
                    for connection in self.state.connections:
                        if self.state.add_connection_to_route(self.state.routes[route_counter], connection):
                            break
            while not self.state.routes[route_counter].is_valid_time(self.state.time_frame):
                self.state.delete_end_connection_from_route(self.state.routes[route_counter])

            route_counter += 1


if __name__ == "__main__":
    from sys import argv, path
    path.append("../classes")
    from state import State

    state = State('../../data/stations_holland.csv', '../../data/routes_holland.csv', 7, 120)
    hillclimber = Hill_climber(state, True)
    
    print(hillclimber.state.show())


        
    





    
