import csv
import time

from code.algorithms.simulated_annealing import *
from code.classes.state import State
from .helpers import *


def experiment_annealing_grid_search(case_name: str, state: 'State', time_seconds: int, cooling_scheme: str, temperature: int):
    """
    does a grid search experiment on the simulated annealing algorithm.

    pre:
        time_seconds is an integer greater than zero
        temperature is an integer greater than zero

    post:
        writes following results to a csv:
            - id
            - score
            - fraction of used connections
            - number of used routes
            - total minutes
            - type of start state (valid or random)
            - type of mutation (light or heavy)
            - list of scores after every iteration
            - sleeper string of last state
    """
    assert time_seconds > 0, "time_seconds should be larger than 0"
    assert temperature > 0, "temperature should be larger than 0"

    with open(f"data/annealing/experiment_annealing_grid_search_{case_name}_{cooling_scheme}_{temperature}.csv", "w") as file:

        writer = csv.writer(file)
        writer.writerow(["run_id",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "start",
                         "mutation",
                         "score_list",
                         "sleeper_string"])

        # configure grid items
        valid_start_state: dict = {'random': False}
        change_light: dict = {'light': True, 'heavy': False}

        # making a valid state for the Netherlands case is skipped,
        # because it takes too long to make such a state
        if case_name != 'netherlands':
            valid_start_state['valid'] = True

        counter: int = 0

        for start_state in valid_start_state:
            for change in change_light:
                sa = Simulated_annealing(
                    state, temperature, 1000, valid_start_state=valid_start_state[start_state])
                start = time.time()

                # run grid element for given amount of time
                while time.time() - start < time_seconds:

                    # run gives list of scores of every iteration
                    score_list = sa.run(
                        counter, cooling_scheme, change_light=change_light[change])

                    writer.writerow(get_csv_row(
                        counter, sa.current_state, start_state, change, list_to_str(score_list)))

                    print(
                        f"SA. Case: {case_name}, cooling scheme: {cooling_scheme}, temperature: {temperature}, counter: {counter}")
                    counter += 1
