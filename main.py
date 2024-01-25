import csv

from sys import argv, path
from code.algorithms.baseline_algorithm import *
from code.scripts.baseline import baseline

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
        max_number_routes = int(argv[2])
        time_frame = int(argv[3])

    # make State object
    state: object = State(file_path_stations,
                          file_path_routes, max_number_routes, time_frame)

    # make a baseline
    baseline(argv[1], state)
