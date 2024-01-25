from .hill_climber import Hill_climber
from math import tanh
import random
import copy


class Plant_Propagation(Hill_climber):

    def __init__(self, state: object, valid_states: bool, population_size: int, max_generations: int, max_nr_runners: int):
        super().__init__(state, valid_states)

        self.population_size = population_size
        self.population: list[object] = []

        self.runner_population: list[object] = []

        self.scores: list[float] = []
        self.converted_fitness_values: list[float: object] = {}

        self.current_generation: int = 1
        self.max_generations = max_generations

        self.max_nr_runners = max_nr_runners

    def initial_population(self) -> None:
        """
        set the initial population by running a certain amount of hill-climber algorithms  
        """
        for i in range(self.population_size):
            self.state.reset()
            self.create_valid_state()
            self.population.append(copy.deepcopy(self.state))

        self.get_scores()

    def get_scores(self) -> None:
        """
        fills self.score with the current population_scores
        """
        for i in range(len(self.population)):
            self.scores.append(self.get_mutated_score(self.population[i]))

    def fitness_function(self) -> list[float]:
        """
        calulate and return the fitness (= normalized score) of the whole population  
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

        for i in range(len(raw_fitness_values)):
            value = raw_fitness_values[i]
            converted_value = (tanh(4 * value - 2) + 1) * 0.5

            converted_values.append([converted_value, self.population[i]])

        # sort population based on fitness scores
        self.converted_fitness_values = sorted(
            converted_values, key=lambda x: x[0], reverse=True)

    def merge_population(self):
        """
        merges the original and runner population
        """
        TODO
        pass

    def get_best_from_population(self) -> None:
        """
        TODO: dit nog aanpassen
        """

        states = [item[1] for item in self.converted_fitness_values]

        # pick the best scores
        new_population = states[:self.population_size]

        # fill self.population with the best scores
        for i in range(len(new_population)):
            self.population[i] = new_population[i]

    def calculate_number_of_runners(self, fitness_value: float) -> int:
        """
        determines the amount of runners per state based on the fitness value
        """
        n_max = self.max_nr_runners
        n_runners = int(n_max * fitness_value)

        return n_runners

    def calculate_distance(self, fitness_value: float) -> float:
        """
        determines the distance for all runners
        """

        r = random.random()
        distance = 2 * (1 - fitness_value) * (r - 0.5)

        return distance

    def likeness(self, original_state: object, new_state: object):
        """
        checks and quantifies the difference between two states
        """
        connections_overlapping = 0
        connections_different = 0

        for original_route in original_state.routes:
            for new_route in new_state.routes:
                original_connections = set(original_route.route_connections)
                new_connections = set(new_route.route_connections)

                connections_overlapping += len(original_connections &
                                               new_connections)
                connections_different += len(original_connections ^
                                             new_connections)

        print(connections_different)

        # pick route_1 from original
        # compare this with all 5 routes from new_state
        # add how many routes are overlapping and how many aren't

    def generate_runner_distances(self):
        """
        Generate all runners
        """
        distance_dict = {}
        # loop p/state
        for i in range(len(self.converted_fitness_values)):
            state = self.converted_fitness_values[i][1]
            value = self.converted_fitness_values[i][0]
            amount_of_runners = self.calculate_number_of_runners(value)

            distance_dict[i] = []

            # loop p/runner
            for j in range(max(amount_of_runners, 1)):
                distance = self.calculate_distance(value)
                distance_dict[i].append(distance)

        return distance_dict

    def make_runners(self):
        """
        creates runner population
        """
        distance_dict = self.generate_runner_distances()

    def run(self):
        # create initial population
        self.initial_population()

        # determine fitness of current population
        self.calculate_converted_fitness()

        # create runner
        self.make_runners()

        # likeness_test
        self.likeness(self.population[0], self.population[1])

        # update population
        self.get_best_from_population()


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
