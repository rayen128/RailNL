from .hill_climber import Hill_climber
from sys import path
path.append("../classes")
from code.classes.state import State

import random
import copy
import math


class Simulated_annealing(Hill_climber):
    def __init__(self, state: 'State', temperature: int, iterations: int, valid_start_state: bool = True) -> None:
        """
        initializes the simulated annealing with a temperature and a amount of iterations

        pre:
            temperature is a positive integer
            state is an empty state

        post:
            all variables are initialized
        """
        super().__init__(state)

        self.valid_start_state = valid_start_state
        self.start_temperature: int = temperature
        self.iterations = iterations

    def calculate_temperature_lineair(self, iteration) -> float:
        """
        calculates the current temperature with a lineair formula

        pre:
            iteration is less than self.iterations

        return:
            the current temperature
        """
        temperature = self.start_temperature - \
            (self.start_temperature / self.iterations) * iteration

        return temperature

    def calculate_temperature_exponential(self, iteration) -> float:
        """
        calculates the current temperature with a exponential formula

        pre:
            iteration is less than self.iterations

        return:
            the current temperature
        """
        temperature = self.start_temperature * (0.997 ** iteration)

        return temperature

    def calculate_temperature_logaritmic(self, iteration) -> float:
        """
        calculates the current temperature with a lineair formula

        pre:
            iteration is less than self.iterations

        return:
            the current temperature
        """
        temperature = self.start_temperature / (1 + (math.log(1 + iteration)))

        return temperature

    def get_chance(self, temperature) -> float:
        """
        calculates the chance a change is going to be accepted

        pre:
            temperature is a positive integer

        return:
            the chance

        """
        # get scores both states
        score_old_state = self.get_score_state(self.current_state)
        score_new_state = self.get_score_state(self.state)

        delta = score_new_state - score_old_state

        # if the score is better, return a 100% acceptance chance
        if delta > 0:
            return 1

        # calculate the accept chance
        chance = 2 ** ((delta) / temperature)
        return chance

    def change_state(self, iteration: int, cooling_scheme: str) -> None:
        """
        changes the state if a random_number is below the accept chance

        pre:
            the iteration is a positive integer
            exponential is a boolean

        post:
            changes the current state if the change is accepted
        """
        # get temperature
        if cooling_scheme == 'exponential':
            temperature = self.calculate_temperature_exponential(iteration)
        elif cooling_scheme == 'lineair':
            temperature = self.calculate_temperature_lineair(iteration)
        elif cooling_scheme == 'logaritmic':
            temperature = self.calculate_temperature_logaritmic(iteration)

        # get accept chance
        accept_chance = self.get_chance(temperature)

        # get random number
        random_number = random.random()

        # decide to accept change or not
        if random_number < accept_chance:
            self.current_state = copy.deepcopy(self.state)
        else:
            self.state = copy.deepcopy(self.current_state)

    def run(self, algorithm_id: int, cooling_scheme: str, change_light: bool = False) -> list[float]:
        """
        runs the simulated annealing algorithm

        pre:
            exponential is a boolean 

        returns:
            list of scores of all iterations
        """
        self.state.reset()
        self.create_state()
        self.current_state = copy.deepcopy(self.state)

        annealing_score_list = []

        for iteration in range(self.iterations):
            if not change_light:
                self.make_change_heavy()
            else:
                self.make_change_light()
            self.change_state(iteration, cooling_scheme)
            annealing_score_list.append(self.current_state.calculate_score())

        return annealing_score_list
