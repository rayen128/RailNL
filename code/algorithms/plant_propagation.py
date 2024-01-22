from .hill_climber import Hill_climber
from math import tanh


class Plant_Propagation(Hill_climber):

    def __init__(self, state: object, valid_states: bool, population_size: int, max_generations: int):
        super().__init__(state, valid_states)
        self.population_size = population_size
        self.population: list[object] = []

        self.current_generation: int = 1
        self.max_generations = max_generations

    def initial_population(self) -> None:
        """
        set the initial population by running a certain amount of hill-climber algorithms  
        """
        for _ in range(self.population_size):
            alg = Hill_climber(self.state)
            solved_state = alg.run()
            self.population.append(solved_state)

    def fitness_function(self) -> list[float]:
        """
        calulate and return the fitness (='score') of the whole population  
        """
        fitness_values = []

        for i in range(len(self.population)):
            fitness_values[i] = self.population[i].score()

        return fitness_values

    def calculate_converted_fitness(self) -> list[float]:
        """
        convert fitness values so that these are mapped to [0,1]
        """
        fitness_values = self.fitness_function()
        converted_values = []

        for i in range(len(fitness_values)):
            value = fitness_values[i]
            converted_value = (tanh(4 * value - 2) + 1) * 0.5
            converted_values.append(converted_value)

        return converted_values

    def likeness(self, state_1, state_2):
        pass

    def make_runners(self):
        pass

    def run(self):
        self.initial_population()
        print(self.self.calculate_converted_fitness())

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
