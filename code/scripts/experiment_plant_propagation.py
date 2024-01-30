import csv
import time

from sys import path
from code.algorithms.plant_propagation import *
from .helpers import *

path.append("code/classes")
from state import State


def grid_search_PPA(state: object, time_seconds: int, case_name: str, initial_population: str, filter_type: str):
    """
    does a grid search based on the PlantPropagation algorithm with the following parameters:

        map: Holland or NL 
        generations
            - Holland: 10, 50, 100
            - NL: 400

        population: 6, 30
        max_runners: 3, 15
        filter_methods: sequential
        starting_states: hill_climber, random OR valid (states)
        time_seconds is per/grid 

    """

    with open(f"data/ppa/experiment_ppa_grid_search_{case_name}_{initial_population}_{filter_type}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["run_id",
                         "start_score",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "initial_population",
                         "generation_count",
                         "population_size",
                         "max_runners",
                         "score_list",
                         "fraction_used_list",
                         "number_of_routes_list",
                         "minutes_list",
                         "sleeper_string"])

        counter = 0

        if case_name == 'holland':
            population_size_list = [6, 12, 30]
            generation_count_list = [10, 50, 100]
            max_runners_list = [3, 7, 15]
        elif case_name == 'netherlands':
            population_size_list = [6, 12, 30]
            generation_count_list = [100, 200, 300]
            max_runners_list = [3, 7, 15]

        for population_size in population_size_list:
            for generation_count in generation_count_list:
                for max_runners in max_runners_list:
                    ppa = Plant_Propagation(
                        state, True, population_size, generation_count, max_runners)

                    ppa.change_population_type(type)

                    start = time.time()

                    # run grid element for given amount of time
                    while time.time() - start < time_seconds:
                        ppa.run()

                        info_list = get_csv_row_ppa(
                            ppa, counter, initial_population, generation_count, population_size, max_runners)

                        writer.writerow(info_list)

                        print(counter)
                        counter += 1


def experiment_best_filter():
    # (short) results showing the best_filter_method
    pass


def experiment_long_ppa():
    # experiment showing that even after many many generations there are increases in scores
    # save ook hoe lang elke generatie erover doet
    pass
