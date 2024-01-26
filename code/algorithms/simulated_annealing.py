from .hill_climber import Hill_climber
from sys import path
path.append("../classes")
from state import State

import random
import copy

class Simulated_annealing(Hill_climber):
    def __init__(self, state: 'State', temperature: int, iterations: int, alpha: float = None) -> None:
        """
        initializes the simulated annealing with a temperature and a amount of iterations

        pre:
            temperature is a positive integer
            state is an empty state

        post:
            all variables are initialized
        """
        super().__init__(state)

        self.start_temperature: int = temperature
        self.iterations = iterations
        self.alpha = alpha

    def calculate_temperature_lineair(self, iteration) -> float:
        """
        calculates the current temperature with a lineair formula

        pre:
            iteration is less than self.iterations

        return:
            the current temperature
        """
        temperature = self.start_temperature - (self.start_temperature / self.iterations) * iteration

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


    def get_chance(self, temperature) -> float:
        """
        calculates the chance a change is going to be accepted

        pre:
            temperature is a positive integer

        return:
            the chance
        
        """
        score_old_state = self.get_score_state(self.current_state)
        score_new_state = self.get_score_state(self.state)

        chance = 2 ** ((score_new_state - score_old_state) / temperature)

        return chance
    
    def change_state(self, iteration: int, exponential: bool) -> None:
        """
        changes the state if a random_number is below the accept chance

        pre:
            the iteration is a positive integer
            exponential is a boolean

        post:
            changes the current state if the change is accepted
        """
        if exponential:
            temperature = self.calculate_temperature_exponential(iteration)
        else:
            temperature = self.calculate_temperature_lineair(iteration)
        
        accept_chance = self.get_chance(temperature)

        random_number = random.random()
        
        if random_number < accept_chance:
            self.current_state = copy.deepcopy(self.state)
        else: 
            self.state = copy.deepcopy(self.current_state)


    def run(self, exponential: bool) -> 'State':
        """
        runs the simulated annealing algorithm

        pre:
            exponential is a boolean 

        returns:
            the state after iteration times of changes
        """
        for iteration in range(self.iterations):
            self.make_change_heavy()
            self.change_state(iteration, exponential)

        return self.current_state

