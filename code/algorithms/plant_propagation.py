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
        self.fitness_values: list[list[float, object]] = []

        self.max_generations = max_generations

        self.max_nr_runners = max_nr_runners
        self.runner_population: list[object] = []

    def run(self):
        # create initial population
        self.initial_population()

        for generation in range(self.max_generations):
            # determine fitness of current population
            self.fitness_function()

            # create runner
            self.make_runners()

            # update population
            self.filter_population()

            # print(f"Generation {generation + 1}: {self.scores}")

    ### SCORE FUNCTIONS ###

    def get_scores(self) -> None:
        """
        fills self.score with the current population_scores and sort the population based on these scores
        """
        for i in range(len(self.population)):
            self.scores.append(self.get_mutated_score(self.population[i]))

        self.sort_population()

    def fitness_function(self) -> list[float]:
        """
        calulate and return the fitness (=normalized score) of the whole population  
        """
        max_score = max(self.scores)
        min_score = min(self.scores)

        for i in range(len(self.population)):
            score = self.population[i].score
            value = 1
            # FIXME: bekijk deze functie nog heeeeul goed (of het uberhaupt boeit btw)
            value = (score - min_score) / (max_score - min_score)
            self.fitness_values.append([value, self.population[i]])

    ### POPULATION FUNCTIONS ###

    def initial_population(self) -> None:
        """
        set the initial population by running a certain amount of hill-climber algorithms  
        """
        hill_climber = Hill_climber(self.state)
        # create the hill-climbers
        for i in range(self.population_size):
            hill_climber.run()
            self.population.append(copy.deepcopy(self.state))

        # populate self.scores
        self.get_scores()

    def filter_population(self) -> None:
        """
        filter the best of the original and runner population 
        """
        self.merge_population()
        self.get_scores()
        self.sort_population()

        next_generation = self.population[:self.population_size]

        self.population = []
        self.scores = []
        self.sorted_fitness_values = []
        self.population = next_generation
        self.get_scores()

    def sort_population(self) -> None:
        """
        sorts the population on score
        """
        # combine scores, population and sort this
        combined_list = list(zip(self.population, self.scores))
        sorted_combined_list = sorted(
            combined_list, key=lambda x: x[1], reverse=True)

        # update scores and population
        self.population = [state for state, score in sorted_combined_list]
        self.scores = [score for state, score in sorted_combined_list]

    def merge_population(self) -> None:
        """
        merge runner and original population
        """
        for runner in self.runner_population:
            self.population.append(runner)

    ### RUNNER METHODS ###

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

                # TODO: Hier heel erg mee spelen op onderzoek gaan
                while abs(distance_goal) > self.likeness(current_state, current_runner):
                    for _ in range(50):
                        current_runner.make_change()
                self.runner_population.append(current_runner)

        print(self.runner_population)

    def generate_runner_distances(self):
        """
        Generate all runners distances
        """
        distance_dict = {}

        # loop over the population
        for i in range(len(self.fitness_values)):
            state = self.fitness_values[i][1]
            value = self.fitness_values[i][0]
            amount_of_runners = max(self.calculate_number_of_runners(value), 1)
            distance_dict[i] = []

            # loop over all runners
            for j in range(amount_of_runners):
                distance = self.calculate_change(value)
                distance_dict[i].append(distance)

        return distance_dict

    def calculate_number_of_runners(self, fitness_value: float) -> int:
        """
        determines the amount of runners per state based on the fitness value
        """
        n_max = self.max_nr_runners
        n_runners = int(n_max * fitness_value)

        return n_runners

    def calculate_change(self, fitness_value: float) -> float:
        """
        determines a distance (semi-random) based on a fitness-value  
        """
        # FIXME: Verander deze (totaal)
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
