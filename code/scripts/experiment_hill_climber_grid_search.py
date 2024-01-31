import csv
import time
from code.algorithms.hill_climber import Hill_climber, Hill_climber_restart
from code.classes.state import State
from .helpers import get_csv_row, list_to_str



def experiment_hill_climber_specific(case_name: str, state: 'State', start_state: str, time_seconds: int) -> None:
    """
    pre:
        time_seconds is an integer greater than zero

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

    with open(f"data/hill_climber/experiment_hill_climber_{case_name}_{start_state}.csv", "w") as file:
        writer = csv.writer(file)

        # write column heads
        writer.writerow(["run_id",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "start",
                         "mutation",
                         "score_list",
                         "sleeper_string"])

        if start_state == 'valid':
            valid_start_state = True
        else:
            valid_start_state = False

        change = 'Heavy'

        counter: int = 0

        hc = Hill_climber(state, valid_start_state)

        start = time.time()

        # run grid element for given amount of seconds
        while time.time() - start < time_seconds:

            # run gives a list with list of results of each iteration
            score_list = hc.run(
                10000, counter, change_light=False)

            # write results to csv
            writer.writerow(get_csv_row(
                counter, hc.current_state, start_state, change, list_to_str(score_list)))

            # show progress to user
            print(
                f"HC. Case: {case_name}, start state: {start_state}, mutation: {change}, counter: {counter}")
            counter += 1


def experiment_hill_climber_grid_search(case_name: str, state: 'State', time_seconds: int) -> None:
    """
    does a grid search experiment on the hill climber algorithm.
    parameters:
        - start state: valid (only for Holland) or random
        - type of mutation: light or heavy

    pre:
        time_seconds is an integer greater than zero

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

    with open(f"data/hill_climber/experiment_hill_climber_grid_search_{case_name}.csv", "w") as file:
        writer = csv.writer(file)

        # write column heads
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

        # do a grid search for every grid item
        for start_state in valid_start_state:
            for change in change_light:
                hc = Hill_climber(
                    state, valid_start_state=valid_start_state[start_state])
                start = time.time()

                # run grid element for given amount of seconds
                while time.time() - start < time_seconds:

                    # run gives a list with list of results of each iteration
                    score_list = hc.run(
                        10000, counter, change_light=change_light[change])

                    # write results to csv
                    writer.writerow(get_csv_row(
                        counter, hc.current_state, start_state, change, list_to_str(score_list)))

                    # show progress to user
                    print(
                        f"HC. Case: {case_name}, start state: {start_state}, mutation: {change}, counter: {counter}")
                    counter += 1


def experiment_hill_climber_restart_grid_search(case_name: str, state: 'State', time_seconds: int) -> None:
    """
    does a grid search experiment on the hill climber algorithm.
    parameters:
        - start state: valid (only for Holland) or random
        - type of mutation: light or heavy

    pre:
        time_seconds is an integer greater than zero
        restart_number is an integer greater than zero

    post:
        writes following results to a csv:
            - id
            - best score found
            - fraction of used connections
            - number of used routes
            - total minutes
            - type of start state (valid or random)
            - type of mutation (light or heavy)
            - list of scores after every iteration
            - sleeper string of state with best score
    """
    assert time_seconds > 0, "time_seconds should be larger than 0"

    with open(f"data/hill_climber_restart/experiment_hill_climber_restart_grid_search_{case_name}.csv", "w") as file:
        writer = csv.writer(file)

        # write column headers
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
        restart_numbers = [100, 250]

        # making a valid state for the Netherlands case is skipped,
        # because it takes too long to make such a state
        if case_name != 'netherlands':
            valid_start_state['valid'] = True

        # the counter is used to show progress to the user
        counter: int = 0

        # run hill climber restart for every combination of grid items
        for restart_number in restart_numbers:
            for start_state in valid_start_state:
                for change in change_light:
                    hcr = Hill_climber_restart(
                        state, restart_number, valid_start_state=valid_start_state[start_state])
                    start = time.time()

                    # run grid element for given amount of time
                    while time.time() - start < time_seconds:

                        # run gives a list with lists of results of each iteration,
                        # and the best score, with the state that belongs to it
                        best_score, best_state, score_list = hcr.run(
                            10000, counter, change_light=change_light[change])

                        writer.writerow(get_csv_row(
                            counter, best_state, start_state, change, list_to_str(score_list), best_score=best_score))

                        # show progress to user
                        print(
                            f"HCR. Case: {case_name}, start state: {start_state}, mutation: {change}, restart number: {restart_number}, counter: {counter}")
                        counter += 1
