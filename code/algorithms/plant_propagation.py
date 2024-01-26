from .hill_climber import Hill_climber
from math import tanh
import random
import copy


class Plant_Propagation(Hill_climber):

    def __init__(self, state: object, valid_states: bool, population_size: int, max_generations: int, max_nr_runners: int):
        super().__init__(state, valid_states)

        self.population_size = population_size
        self.population: list[object] = []

        self.scores: list[float] = []
        self.sorted_fitness_values: list[float: object] = {}

        self.current_generation: int = 1
        self.max_generations = max_generations

        self.max_nr_runners = max_nr_runners
        self.runner_population: list[object] = []

    def initial_population(self) -> None:
        """
        set the initial population by running a certain amount of hill-climber algorithms  
        """
        # create the hill-climbers
        for i in range(self.population_size):
            self.state.reset()
            self.create_valid_state()
            self.population.append(copy.deepcopy(self.state))

        # populate self.scores
        self.get_scores()

    def get_scores(self) -> None:
        """
        fills self.score with the current population_scores
        """
        for i in range(len(self.population)):
            self.scores.append(self.get_mutated_score(self.population[i]))

    def fitness_function(self) -> list[float]:
        """
        calulate and return the fitness (=normalized score) of the whole population  
        """
        max_score = max(self.scores)
        min_score = min(self.scores)

        raw_fitness_values = []

        for i in range(len(self.population)):
            score = self.population[i].score
            value = (max_score - score) / (max_score - min_score)
            raw_fitness_values.append(value)

        return raw_fitness_values

    def calculate_converted_fitness(self) -> list[float]:
        """
        convert fitness-values so that these are mapped to [0,1]
        """
        raw_fitness_values = self.fitness_function()
        converted_values = []

        # convert fitness values
        for i in range(len(raw_fitness_values)):
            value = raw_fitness_values[i]
            converted_value = (tanh(4 * value - 2) + 1) * 0.5

            converted_values.append([converted_value, self.population[i]])

        # sort population based on fitness scores
        self.sorted_fitness_values = sorted(
            converted_values, key=lambda x: x[0], reverse=True)

    def merge_population(self) -> None:
        """
        merge runner and original population
        """
        for runner in self.runner_population:
            self.population.append(runner)

    def filter_population(self) -> None:
        """
        filter the best of the original and runner population 
        """
        self.merge_population()
        self.get_scores()

    def calculate_number_of_runners(self, fitness_value: float) -> int:
        """
        determines the amount of runners per state based on the fitness value
        """
        n_max = self.max_nr_runners
        n_runners = int(n_max * fitness_value)

        return n_runners

    def calculate_distance(self, fitness_value: float) -> float:
        """
        determines a distance (semi-random) based on a fitness-value  
        """
        r = random.random()
        distance = 2 * (1 - fitness_value) * (r - 0.5)

        return distance

    def count_route_difference(self, original_state: object, new_state: object):
        """
        checks and checks the route differences between two states
        """
        connections_overlapping = 0
        connections_different = 0

        routes_used = []
        connection_counter = 0

        for original_route in original_state.routes:

            max_overlap = -1
            best_match = None
            original_connections = set(original_route.connection_ids)

            connection_counter += len(original_connections)

            for new_route in new_state.routes:
                if new_route not in routes_used:
                    new_connections = set(new_route.connection_ids)

                    overlap = len(
                        original_connections.intersection(new_connections))

                    if overlap > max_overlap:
                        max_overlap = overlap
                        difference = len(original_connections.symmetric_difference(
                            new_connections))
                        best_match = new_route

            if best_match:
                routes_used.append(best_match)
                connections_different += difference
                connections_overlapping += max_overlap

        proportion = connections_overlapping / connection_counter

        return connections_different, connections_overlapping, proportion

    def likeness(self, original_state: object, new_state: object):
        """
        quantifies the difference between two states
        """
        connections_different, connections_overlapping, proportion = self.count_route_difference(
            original_state, new_state)

        return proportion

    def generate_runner_distances(self):
        """
        Generate all runners
        """
        distance_dict = {}

        # loop over the population
        for i in range(len(self.sorted_fitness_values)):
            state = self.sorted_fitness_values[i][1]
            value = self.sorted_fitness_values[i][0]
            amount_of_runners = self.calculate_number_of_runners(value)

            distance_dict[i] = []

            # loop over all runners
            for j in range(max(amount_of_runners, 1)):
                distance = self.calculate_distance(value)
                distance_dict[i].append(distance)

        return distance_dict

    def make_runners(self):
        """
        creates runner population
        """
        distance_dict = self.generate_runner_distances()

        # loop over population
        for state_index in range(len(self.population)):
            # loop over all runners
            current_state = self.population[state_index]

            for runner_index in range(len(distance_dict[state_index])):
                distance_goal = distance_dict[state_index][runner_index]

                current_runner = copy.deepcopy(current_state)

                while abs(distance_goal) > self.likeness(current_state, current_runner):
                    for _ in range(50):
                        current_runner.make_change()
                self.runner_population.append(current_runner)

        print(f"Size of population is: {len(self.population)}")

    def run(self):
        # create initial population
        self.initial_population()

        for generation in range(self.max_generations):
            # determine fitness of current population
            self.calculate_converted_fitness()

            # create runner
            self.make_runners()

            # update population
            self.filter_population()


# Vragen (voor Quinten?):
    # normalization van fitness_function?
    # grootte N_max (= number of max runners)?
    # rond ik naar boven of naar onder af bij #_of_runners

# Exploration vs. Exploitation


# Variables:
# the population size (=De start hoeveelheid HCs & max hoeveelheid states)
# the (max) number of generations (=g_max)
# a fitness function (f())
# the number of runners to create for each solution
# the distance for each runner


# Nr. of shoots = m

# All shoots send out runners p/itteration
# --> This provides a terminating criterion and is represented by g_max.

# Fitness-function [0,1] = hoe 'goed' een solution is & dus based op de doel-functie
# --> Map fitness function (f(x)) on the following N(x) = 1/2 (tanh (4f(x) − 2) + 1)

# Number of runners = n_r = [nmax N_ir]
# --> n_max is max number of runners to generate (=population size?)

# d_(r,j) = 2(1 − N_i)(r − 0.5)
# for j = 1, . . . , n, where n is the dimension of the search space.
