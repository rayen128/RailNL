from sys import path
from typing import Union

path.append("code/classes")
from code.classes.state import State


def list_to_str(score_list):
    """
    gives str of scores, to put inside csv row for grid search results

    returns:
        str of all scores, delimited by '~'
    """
    score_str = ""
    for index, score in enumerate(score_list):
        score_str += str(score)
        if index < len(score_list) - 1:
            score_str += "~"
    return score_str


def get_csv_row(id: int, state: 'State', start: str, mutation: str, score_str: str, best_score: float = 0.0) -> list:
    """
    gives row to write to grid search results csv

    returns:
        list with row values
    """
    if best_score:
        score = best_score
    else:
        score = state.calculate_score()
    return [id,
            score,
            state.fraction_used_connections,
            state.number_routes,
            state.total_minutes,
            start,
            mutation,
            score_str,
            state.show_sleeper_string()]


def get_csv_row_ppa(ppa: object, counter: int, initial_population: str, generation_count: int, population_size: int, max_runners: int) -> list[Union[int, list[float]]]:
    """
    gives row to write to grid search results csv specific for the plant propagation algorithm
    """
    info_list = [counter, ppa.start_score,
                 ppa.high_score, ppa.best_state.fraction_used_connections,
                 ppa.best_state.number_routes, ppa.best_state.total_minutes,
                 initial_population, generation_count, population_size, max_runners,
                 list_to_str(ppa.high_scores),
                 list_to_str(ppa.fraction_scores),
                 list_to_str(ppa.routes_scores),
                 list_to_str(ppa.minute_scores),
                 ppa.best_state.show_sleeper_string()]

    return info_list
