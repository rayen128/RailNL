from math import tanh
import random
import copy

from .hill_climber import Hill_climber
from typing import Union
from ..visualisation.visualisation import *


class Plant_Propagation(Hill_climber):

    def __init__(self, state: object, valid_states: bool, population_size: int, max_generations: int, max_nr_runners: int, max_connection_returns: int = 0):
        """
        initializes the plant propagation algorithm (PPA) with the following parameters: 
            population_size
            amount of generations
            max_runners


        pre: 
            state is a state object
            population_size is an integer
            max_runners an integer

        post:
            PPA object is created with all necesarry aspects
            the PPA is ready to be run
        """
        super().__init__(state, valid_states, max_connection_returns=max_connection_returns)

        # all population and generation variables
        self.population_size = population_size
        self.population: list[object] = []
        self.max_generations = max_generations

        # scores lists
        self.scores: list[float] = []
        self.fitness_values: list[list[float, object]] = []

        # lists to save results in
        self.high_scores: list[float] = []
        self.fraction_scores: list[float] = []
        self.routes_scores: list[int] = []
        self.minute_scores: list[int] = []

        # all runner-related variables
        self.max_nr_runners = max_nr_runners
        self.runner_population: list[object] = []

        # choose: valid, random, hill_climber
        self.initial_population_type = 'hill_climber'

        # save how many connections can be returned
        self.max_connection_returns = 0

        # saves overall highest achieved score
        self.start_score: float = 0
        self.high_score: float = 0
        self.best_state = self.state

        # tournament size (potentially) affects population_filter method
        self.tournament_size = 2

        # choose: best, sequential or random
        self.filter_type = 'sequential'

        # heuristic(s)
        self.no_return_connection_heuristic = False

    ### GENERAL FUNCTIONS ###

    def run(self) -> None:
        """
        runs the algorithm

        post:
            information of best found state is saved
        """

        # reset the state
        self.reset()

        # create initial population
        self.initial_population()

        # run the algorithm generation amount time
        for generation in range(self.max_generations):
            # get all scores of the current population
            self.get_scores()

            # determine fitness of current population
            converge_status = self.fitness_function()

            # check if population has converged to a certain local optimum
            if converge_status == 'converged':
                return generation

            # create runner
            self.make_runners()

            # update population
            self.filter_population(self.filter_type, generation)

            print(f"Generation {generation + 1}: {self.high_score}")
            print(f"p= {self.best_state.fraction_used_connections}")

            # save most important info of best_state
            self.add_info()

    def reset(self) -> None:
        """
        resets class by clearing all (relevant) variables

        post:
            all variables listed down-below are cleared 
        """
        self.scores = []
        self.sorted_fitness_values = []
        self.population = []
        self.runner_population = []
        self.high_score = 0
        self.high_scores = []
        self.fraction_scores = []
        self.routes_scores = []
        self.minute_scores = []

    def initial_population(self) -> None:
        """
        set the initial population. type is based on self.initial_population_type

        options are:
            'valid' (semi-randomly created valid states)
            'random' (completely random states)
            'hill_climber' (hill_climbers)

        pre: 
            initial_population_type is one of the options above 

        post:
            prints informative message to terminal
            starting population is created
        """
        # set population type
        type = self.initial_population_type

        print(f"creating the initial {type}-population")
        print('...')

        # create valid_state population
        if type == 'valid':
            for i in range(self.population_size):
                self.state.reset()
                self.create_valid_state()
                self.population.append(copy.deepcopy(self.state))
        # create random_state population
        elif type == 'random':
            for i in range(self.population_size):
                self.state.reset()
                self.create_random_state(static=True)
                self.population.append(copy.deepcopy(self.state))
        # create hill_climber population
        elif type == 'hill_climber':
            state = Hill_climber(
                self.state, False, self.max_connection_returns)

            # run hill_climbers
            for i in range(self.population_size):
                state.run(1000, 1)
                self.population.append(copy.deepcopy(state.current_state))

        elif type == 'hill_climber_valid':
            state = Hill_climber(
                self.state, True, self.max_connection_returns)

            # run hill_climbers
            for i in range(self.population_size):
                state.run(1000, 1)
                self.population.append(copy.deepcopy(state.current_state))

    def change_population_type(self, type: str) -> None:
        """
        method to change intitial population-type

        pre:
            type is either random, valid or hill_climber

        post:
            initial_population_type is changed
        """
        self.initial_population_type = type

    def add_info(self):
        """
        saves the most important information off the best state, is used to save/write out info for experiments

        post:
            all variables down-below are added to it respective list  
        """
        self.high_scores.append(self.high_score)
        self.fraction_scores.append(self.best_state.fraction_used_connections)
        self.routes_scores.append(self.best_state.number_routes)
        self.minute_scores.append(self.best_state.total_minutes)

    ### SCORE FUNCTIONS ###

    def get_scores(self) -> None:
        """
        fills self.score with the current population_scores

        pre: 
            self.population is filled with (full) states

        post: 
            self.scores is populated by tuples with the corresponding (score, state)
        """
        # loop over population
        for i in range(len(self.population)):

            # append info to self.scores
            self.scores.append([self.get_mutated_score(
                self.population[i]), self.population[i]])

    def fitness_function(self) -> Union[None, str]:
        """
        calulates the fitness (=normalized score) of the whole population, used for distance calculation 

        calculation is with the following formula:
            (state_score - lowest score) / (highest score - lowest score) 

        pre:
            self.scores is (correctly) filled with (score, state) tuples
            minimum & maximum are not the same

        post:
            self.fitness_values is populated with tuples consisting of:
                (fitness_values, state, absolute_score)


        """
        # Extract just the scores from self.scores
        scores_only = [score_state_pair[0] for score_state_pair in self.scores]

        # Now find the max and min scores
        max_score = max(scores_only)
        min_score = min(scores_only)

        # if scores are equal end algorithm by returning exit-statement
        if max_score == min_score:
            print(f'Algorithm converged to a score of: {self.high_score}')
            return 'converged'

        for i in range(len(self.population)):
            score = self.scores[i][0]
            value = (score - min_score) / (max_score - min_score)
            self.fitness_values.append([value, self.scores[i][1], score])

    def update_high_score(self, score: float, state: object) -> None:
        """
        checks if provided score is the high-score and updates accordingly

        pre:
            score is a float
            state is a state

        post:
            if score is higher than current high_score, update this
        """
        if score > self.high_score:
            self.high_score = score
            self.best_state = state

    def set_start_score(self, score: float) -> None:
        """
        saves a score as start score, is used to save (best) score of generation 1

        pre:
            score is a float

        post:
            self.start_score has this score

        """
        self.start_score = score

    ### POPULATION FUNCTIONS ###

    def filter_population(self, filter_type: str, generation, visualize_states: bool = False) -> None:
        """
        filters the (best of) the current population using the selected filter_method 
        if set visualize is set to True, also visualizes whole population

        options are:
            'best': (select the highest scoring-states)
            'random' (tournament-style, randomly select buckets)
            'sequential' (tournament-style, loops over population for buckets) 
        """
        # add runners to population
        self.merge_population()

        # potentially visualize states
        if visualize_states:
            for state in self.population:
                show_plot(self.station_dict, state, 'netherlands')

        # calculate all scores
        self.get_scores()

        # clear population
        self.population = []

        # apply the 'best' filter
        if filter_type == 'best':
            high_score = self.filter_population_best_only()

        elif filter_type == 'sequential' or filter_type == 'random':

            # set bucket_size
            tournament_size = self.tournament_size

            # apply the sequential filter
            if filter_type == 'sequential':
                high_score = self.filter_population_sequential(tournament_size)

            # apply the random filter
            else:
                high_score = self.filter_population_random(tournament_size)

        # set the start_score if applicable
        if generation == 0:
            self.set_start_score(high_score)

        self.scores = []
        self.sorted_fitness_values = []

    def filter_population_best_only(self) -> tuple[float, object]:
        """
        filter method that only chooses highest scoring-states & (potentially) update high_score

        pre:
            self.scores is populated with (score, state) tuples

        post:
            population is back to population_size
            only highest performing states are left

        returns:
            highest performing score & state
        """
        # sort self.scores
        sorted_scores = sorted(
            self.scores, key=lambda item: item[0], reverse=True)

        # get the highest scoring states
        for state in sorted_scores[:self.population_size]:
            self.population.append(state[1])

        # save & update high_score
        high_score = sorted_scores[0][0]
        self.update_high_score(high_score, sorted_scores[0][1])

        return high_score

    def filter_population_sequential(self, tournament_size: int) -> tuple[float, object]:
        """
        tournament-style filter that sequentially loops through the population

        TIP: if population_size is dividable by tournament_size, the whole population willtaken into account

        pre:
            self.scores is populated with (score, state) tuples

        post:
            population is back to population_size
            all the highest scoring states p/bucket are left

        returns:
            highest performing score & state

        """
        # shuffle the scores list to ensure randomness
        random.shuffle(self.scores)

        # index variable to keep track
        tournament_index = 0

        # loop until population_size is reached or too little scores are left
        while len(self.population) < self.population_size and tournament_index < len(self.scores):

            # select a group
            tournament = self.scores[tournament_index:
                                     tournament_index + tournament_size]

            # pick highest score as winner
            winner = max(tournament, key=lambda x: x[0])

            # update tournament_index
            tournament_index += tournament_size

            # update high-score
            self.update_high_score(winner[0], winner[1])

            # add winner to population of the next generation
            self.population.append(winner[1])

        return self.high_score

    def filter_population_random(self, tournament_size: int) -> tuple[float, object]:
        """
        tournament-style filter that semi randomly filters through population based on score. 

        pre:
            self.scores is populated with (score, state) tuples

        post:
            population is back to population_size
            all the highest scoring states p/bucket are left

        returns:
            highest performing score & state

        """
        while len(self.population) < self.population_size:
            # ensure tournament_size doesn't exceed number of remaining states
            current_tournament_size = min(tournament_size, len(self.scores))

            # pick winner of randomly chosen states
            tournament = random.sample(self.scores, current_tournament_size)
            winner = max(tournament, key=lambda x: x[0])

            # update high-score
            self.update_high_score(winner[0], winner[1])

            # add winner to population of the next generation
            self.population.append(winner[1])

            # remove from scores (so that it is not chosen anymore)
            self.scores.remove(winner)

        return self.high_score

    def merge_population(self) -> None:
        """
        adds all created runners to the original population

        pre:
            self.runner_population is populated with states

        post:
            self.population now also includes runners
        """
        for runner in self.runner_population:
            self.population.append(runner)

    ### RUNNER METHODS ###

    def make_runners(self):
        """
        creates all the runners for all states in the population based on distance and amount of runners p/state
        """
        # generate all distances for all parent states in current population
        distance_dict = self.generate_runner_distances()

        # loop over population
        for state_index in range(len(self.population)):

            # set current used state
            current_state = self.population[state_index]

            # loop over all runners
            for runner_index in range(len(distance_dict[state_index])):

                # set goal
                distance_goal = distance_dict[state_index][runner_index]

                # set current runner
                current_runner = copy.deepcopy(current_state)
                self.state = current_runner

                # set counter and max_amount of changes
                counter = 0
                max_changes = 300

                # do changes until distance is reached or counter is exceeded
                while distance_goal > self.likeness(current_state, self.state) and counter < max_changes:
                    for i in range(distance_goal):

                        # calculate the proportion of used connections
                        p = self.state.fraction_used_connections

                        if p < 0.8:
                            self.make_change_heavy()
                        else:
                            self.make_change_light()
                        counter += 1

                self.runner_population.append(self.state)

    def generate_runner_distances(self):
        """
        Generate all runners distances
        """
        distance_dict = {}

        # loop over the population
        for i in range(len(self.fitness_values)):
            value = self.fitness_values[i][0]
            state = self.fitness_values[i][1]
            score = self.fitness_values[i][2]

            amount_of_runners = max(
                self.calculate_number_of_runners(value), 1)
            distance_dict[i] = []

            # loop over all runners
            for j in range(amount_of_runners):
                distance = self.calculate_distance(value, score)
                distance_dict[i].append(distance)

        return distance_dict

    def calculate_number_of_runners(self, fitness_value: float) -> int:
        """
        determines the amount of runners per state based on the fitness value
        """
        n_max = self.max_nr_runners
        n_runners = int(n_max * fitness_value)

        return n_runners

    def calculate_distance(self, fitness_value: float, score: float) -> float:
        """
        determines a distance (semi-random) based on a fitness-value  
        """
        scale_factor = 10
        variability = scale_factor / 2
        r = random.random()

        distance = max(int((1 - fitness_value) *
                       scale_factor + int(r * variability)), 1)

        return distance

    def count_route_difference(self, original_state: object, new_state: object):
        """
        counts the route differences between two states
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
                routes_used.append(original_route)
                routes_used.append(best_match)
                connections_different += difference
                connections_overlapping += max_overlap

        if original_state.number_routes != new_state.number_routes:
            bigger_state = max(original_state, new_state,
                               key=lambda state: state.number_routes)

            for route in bigger_state.routes:
                if route not in routes_used:
                    connections_different += len(set(route.connection_ids))

        proportion = connections_overlapping / connection_counter

        return connections_different, connections_overlapping, proportion

    def likeness(self, original_state: object, new_state: object):
        """
        quantifies the difference between two states
        """
        connections_different, connections_overlapping, proportion = self.count_route_difference(
            original_state, new_state)

        return connections_different
