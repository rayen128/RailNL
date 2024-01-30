import csv

from code.algorithms.baseline_algorithm import *

from code.classes.state import State


def baseline(case_name: str, state: 'State') -> None:
    baseline_alg = Baseline_Algorithm(state)
    with open(f"data/baseline_data_{case_name}.csv", "w") as file:
        writer = csv.writer(file)

        # write column headers
        writer.writerow(["state_id", "algorithm", "score", "fraction_used_connections",
                        "number_routes", "total_minutes", "is_solution", "sleeper_string"])

        # baseline algorithm 1
        for i in range(10001):
            state.reset()
            baseline_alg.baseline_algorithm_1()
            writer.writerow(state.show_csv_line(i, "random_algorithm_1"))

        # baseline algorithm 2
        for j in range(10000, 20001):
            state.reset()
            baseline_alg.baseline_algorithm_2()
            writer.writerow(state.show_csv_line(j, "random_algorithm_2"))

        # baseline algorithm 3
        for k in range(20000, 30001):
            state.reset()
            baseline_alg.baseline_algorithm_3()
            writer.writerow(state.show_csv_line(k, "random_algorithm_3"))
