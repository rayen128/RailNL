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
                         "sleeper_string"])

        counter = 0

        for population_size in [6, 12, 30]:
            for generation_count in [10, 50, 100]:
                for max_runners in [3, 7, 15]:
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
                                     list_to_str(ppa.high_scores), ppa.best_state.show_sleeper_string()]

                        writer.writerow(info_list)

                        print(counter)
                        counter += 1

                        # get_csv_row met daarin:
                        # ppa.high_score (elke keer weer)
                        # ppa.high_score (uiteindelijke)
                        # sleeper-string


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
    pass
