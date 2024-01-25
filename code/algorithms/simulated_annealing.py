from .hill_climber import Hill_climber
from sys import path
path.append("../classes")
from state import State

import random
import copy

class Simulated_annealing(Hill_climber):
    def __init__(self, state: 'State', temperature: int, iterations: int, alpha: float = None):
        super().__init__(state)

        self.start_temperature: int = temperature
        self.iterations = iterations
        self.alpha = alpha

    def calculate_temperature_lineair(self, iteration):
        temperature = self.start_temperature - (self.start_temperature / self.iterations) * iteration

        return temperature

    def calculate_temperature_exponential(self, iteration):
        temperature = self.start_temperature * (0.997 ** iteration)

        return temperature


    def get_chance(self, temperature):
        score_old_state = self.get_score_state(self.current_state)
        score_new_state = self.get_score_state(self.state)

        chance = 2 ** ((score_new_state - score_old_state) / temperature)

        return chance
    
    def change_state(self, iteration: int, exponential: bool):
        if exponential:
            temperature = self.calculate_temperature_exponential(iteration)
        else:
            temperature = self.calculate_temperature_lineair(iteration)
        
        accept_chance = self.get_chance(temperature)

        random_number = random.random()
        
        if random_number < accept_chance:
            print('accepted!')
            self.current_state = copy.deepcopy(self.state)
        else: 
            self.state = copy.deepcopy(self.current_state)


    def run(self, exponential: bool):
        for iteration in range(self.iterations):
            self.make_change()
            print(self.state.calculate_score())
            self.change_state(iteration, exponential)

        return self.current_state

