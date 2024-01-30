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
                         "sleeper_string",
                         "heuristic_value"])

        counter = 0

        if case_name == 'holland':
            population_size_list = [6, 12, 30]
            generation_count_list = [10, 50, 100]
            max_runners_list = [3, 7, 15]
            heuristic_list = 0
        elif case_name == 'netherlands':
            population_size_list = [12, 30]
            generation_count_list = 200
            max_runners_list = [3, 15]
            heuristic_list = [0, 1, 2]

        for population_size in population_size_list:
            for generation_count in generation_count_list:
                for max_runners in max_runners_list:
                    for heuristic_value in heuristic_list:
                        ppa = Plant_Propagation(
                            state, True, population_size, generation_count, max_runners)

                        ppa.change_population_type(type)
                        ppa.max_connection_returns = heuristic_value

                        start = time.time()

                        # run grid element for given amount of time
                        while time.time() - start < time_seconds:
                            ppa.run()

                            info_list = get_csv_row_ppa(
                                ppa, counter, initial_population, generation_count, population_size, max_runners)

                            info_list.append(heuristic_value)

                            writer.writerow(info_list)

                            print(counter)
                            counter += 1


def experiment_best_filter(state: object, time_seconds: int, case_name: str, initial_population: str):
    """
    NL
    3 filters
    30 400 7
    12 400 15
    """

    if case_name != 'netherlands':
        print('pick netherlands as case')
        return False
    else:
        population_size_list = [12, 30]
        max_runners_list = [15, 7]
        generation_count = 200

    counter = 0

    for filter_type in ['best', 'random']:
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

            for i in range(2):
                population_size = population_size_list[i]
                max_runners = max_runners_list[i]

                start = time.time()

                ppa = Plant_Propagation(
                    state, True, population_size, generation_count, max_runners)

                while time.time() - start < time_seconds:
                    ppa.run()

                    info_list = get_csv_row_ppa(
                        ppa, counter, initial_population, generation_count, population_size, max_runners)

                    writer.writerow(info_list)

                    print(counter)
                    counter += 1


def experiment_long_ppa(state: object, case_name: str, initial_population: str, filter_type: str):
    """
    NL
    30 10000 7
    12 10000 15
    """
    with open(f"data/ppa/experiment_ppa_grid_search_{case_name}_{initial_population}_{filter_type}_5000generations.csv", "w") as file:
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
                         "sleeper_string",
                         "time_taken"])

        counter = 0

        if case_name != 'netherlands':
            print('pick netherlands as case')
            return False
        else:
            population_size_list = [12, 30]
            max_runners_list = [15, 7]
            generation_count = 5000

        while True:
            start = time.time()
            index = counter % 2
            ppa = Plant_Propagation(
                state, True, population_size_list[index], generation_count, max_runners_list[index])

            ppa.run()

            info_list = get_csv_row_ppa(
                ppa, counter, initial_population, generation_count, population_size_list[index], max_runners_list[index])

            end = time.time() - start
            info_list.append(end)

            writer.writerow(info_list)

            print(counter)
            counter += 1

    # experiment showing that even after many many generations there are increases in scores
    # save ook hoe lang elke generatie erover doet
    pass
