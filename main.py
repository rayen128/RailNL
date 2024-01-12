from sys import argv, path
from code.algorithms.random_algorithm import random_algorithm_1

path.append("code/classes")
from state import State

if __name__ == "__main__":

    # make sure a .csv is given for both stations and routes
    if (len(argv) != 2 or (argv[1].lower() != "holland" or argv[1].lower() != "netherlands")) and len(argv) != 4:
        print("Usage: representation.py [filename] [max number of routes] [time frame]")
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
    state: object = State(file_path_stations, file_path_routes, max_number_routes, time_frame)

    random_algorithm_1(state)

