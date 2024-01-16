import csv

from sys import argv, path
from code.algorithms.random_algorithm import *

path.append("code/classes")
from state import State

if __name__ == "__main__":
    # make sure a .csv is given for both stations and routes
    if (len(argv) != 2 or (argv[1].lower() != "holland" and argv[1].lower() != "netherlands")) and len(argv) != 4:
        print(
            "Usage: main.py [case name] [max number of routes] [time frame]")
        exit()

    file_path_stations = f"data/stations_{argv[1]}.csv"
    file_path_routes = f"data/routes_{argv[1]}.csv"

    if argv[1].lower() == "holland":
        max_number_routes = 7
        time_frame = 120

    elif argv[1].lower() == "netherlands":
        max_number_routes = 20
        time_frame = 180

    else:
        max_number_routes = argv[2]
        time_frame = argv[3]

    # make State object
    state: object = State(file_path_stations,
                          file_path_routes, max_number_routes, time_frame)

    score, route, description = random_algorithm_2(state)

    state.write_output("data/output.csv")
    print(f"Score: {score}")
    print(f"Route: {route}")
    print(f"Description:\n{description}")
    print(f"Sleeper string:\n {state.show_sleeper_string()}")
    print(f"csv line: {state.show_csv_line(0, 'random_algorithm_2')}")

    with open(f"data/baseline_data_{argv[1]}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["state_id", "algorithm", "score", "fraction_used_connections",
                        "number_routes", "total_minutes", "sleeper_string"])

        for i in range(10000):
            state.reset()
            random_algorithm_1(state)
            writer.writerow(state.show_csv_line(i, "random_algorithm_1"))

        for j in range(10001, 20000):
            state.reset()
            random_algorithm_2(state)
            writer.writerow(state.show_csv_line(j, "random_algorithm_2"))

        for k in range(20001, 30000):
            state.reset()
            random_algorithm_3(state)
            writer.writerow(state.show_csv_line(k, "random_algorithm_3"))
