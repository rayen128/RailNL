from algorithm import Algorithm
import random
import copy
from sys import path

class Hill_climber(Algorithm):
    def __init__(self, state: object, valid_start_state: bool = True):
        super().__init__(state)
        self.valid_start_state = valid_start_state
        self.state_list = []

        self.create_state()

        self.old_state = copy.deepcopy(self.state)

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


    def make_change(self):
        random_number = random.randint(0, 100)
        if not self.choose_route_to_add_connection() and \
            self.state.number_routes < self.state.max_number_routes:
            if random_number <= 45:
                self.delete_random_connection()
            elif random_number >= 46 and random_number <= 80:
                self.add_random_route()
            else:
                self.delete_random_route()

        elif not self.choose_route_to_add_connection() and \
            self.state.number_routes >= self.state.max_number_routes:
            if random_number <= 65:
                self.delete_random_connection()
            else:
                self.delete_random_route()

        elif self.state.number_routes < self.state.max_number_routes:
            if random_number <= 35:
                self.delete_random_connection()
            elif random_number >= 36 and random_number <= 60:
                route_number = self.choose_route_to_add_connection()
                self.add_random_connection(route_number)
            elif random_number >= 61 and random_number <= 85:
                self.add_random_route()
            else:
                self.delete_random_route()

        elif self.state.number_routes >= self.state.max_number_routes:
            if random_number <= 45:
                self.delete_random_connection()
            elif random_number >= 46 and random_number <= 75:
                route_number = self.choose_route_to_add_connection()
                self.add_random_connection(route_number)
            else:
                self.delete_random_route()
            
    def get_score_state(self, state: 'State'):
        score = state.calculate_score()
        
        if not state.is_valid_solution():
            score -= 1000
        
        return score
    
    def compare_scores_state(self):
        score_new_state = self.get_score_state(self.state)
        score_old_state = self.get_score_state(self.old_state)

    
    def choose_route_to_add_connection(self) -> int:
        routes_able_to_add_connection = []
        for index in range(self.number_routes - 1):
            if self.routes[index].total_time <= self.time_frame - 20:
                routes_able_to_add_connection.append(index)
        
        random_route = random.choice(routes_able_to_add_connection)

        return random_route
            
        

if __name__ == "__main__":
    from sys import argv, path
    path.append("../classes")
    from state import State

    state = State('../../data/stations_holland.csv', '../../data/routes_holland.csv', 7, 120)
    hillclimber = Hill_climber(state, True)
    
    
    print(hillclimber.state.show())


        
    





    
