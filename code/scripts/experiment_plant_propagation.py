import csv
import time

from sys import path
from code.algorithms.plant_propagation import *
from .helpers import *

path.append("code/classes")
from state import State


def grid_search_PPA_hill_climber(state: object, time_seconds: int, case_name: str, initial_population: str, filter_type: str):
    # Map: holland & NL
    # Generations: 10, 50, 100
    # Population: 6, 12, 30
    # Max_runners: 3, 7, 15
    # Filter_methods: sequential
    # Starting_states: Hill-Climbers
    # 15 min p/grid

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

                    start = time.time()

                    # run grid element for given amount of time
                    while time.time() - start < time_seconds:
                        ppa.run()

                        info_list = [counter, ppa.start_score,
                                     ppa.high_score, ppa.best_state.fraction_used_connections,
                                     ppa.best_state.number_routes, ppa.best_state.total_minutes,
                                     initial_population, generation_count, population_size, max_runners,
                                     list_to_str(ppa.high_scores),
                                     list_to_str(ppa.fraction_scores),
                                     list_to_str(ppa.routes_scores),
                                     list_to_str(ppa.minute_scores),
                                     ppa.best_state.show_sleeper_string()]

                        writer.writerow(info_list)

                        print(counter)
                        counter += 1


def grid_search_PPA_random():
    # Map: holland & NL
    # Generations: 10, 50, 100
    # Population: 6, 12, 30
    # Max_runners: 3, 7, 15
    # Filter_methods: sequential
    # Starting_states: random
    # 15 min p/grid
    pass


def experiment_best_filter():
    # (short) results showing the best_filter_method
    pass


def experiment_long_ppa():
    # experiment showing that even after many many generations there are increases in scores
    # save ook hoe lang elke generatie erover doet
    pass
