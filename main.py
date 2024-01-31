from sys import argv

from code.algorithms.hill_climber import Hill_climber, Hill_climber_restart
from code.algorithms.simulated_annealing import Simulated_annealing
from code.algorithms.plant_propagation import Plant_Propagation

from code.visualisation import visualisation

from code.classes.state import State


def create_state(case_name: str) -> 'State':
    """
    creates State object, based on case name.

    pre:
        case name is 'holland' or 'netherlands'
    """
    assert case_name == "holland" or case_name == "netherlands", \
        f"invalid case name: {case_name}"

    file_path_stations: str = f"data/stations_{case_name}.csv"
    file_path_routes: str = f"data/routes_{case_name}.csv"

    # get correct contraints per case
    if case_name == "holland":
        max_routes: int = 7
        timeframe: int = 120
    elif case_name == "netherlands":
        max_routes: int = 20
        timeframe: int = 180

    state = State(file_path_stations, file_path_routes, max_routes, timeframe)

    return state


def run_hillclimber(state: 'State', valid_start_state: bool) -> 'State':
    """
    runs a hillclimber algorithm and returns endstate

    returns:
        State object
    """
    hc = Hill_climber(state, valid_start_state=valid_start_state)
    hc.run(10000, 0)
    return hc.current_state


def run_hillclimber_restart(state: 'State', valid_start_state) -> 'State':
    """
    runs a hillclimber restart algorithm and returns state with best result

    returns: 
        State object
    """
    restarts: int = int(input(
        "After how many same scores should the algorithm restart? (recommended: 50) "))
    hcr = Hill_climber_restart(
        state, restarts, valid_start_state=valid_start_state)
    score, best_state, scorelist = hcr.run(10000, 0)
    return best_state


def run_simulated_annealing(state: 'State', valid_start_state: bool) -> 'State':
    """
    runs a simulated annealing algorithm and returns endstate

    returns: 
        State object
    """
    temperature: int = int(
        input("Pick a temperature for simulated annealing. (recommended: 200) "))
    cooling_scheme: str = input(
        "Pick a cooling scheme. (possibilities: lineair, exponential, logaritmic) ")
    assert cooling_scheme == 'lineair' or cooling_scheme == 'exponential' or cooling_scheme == 'logaritmic', "wrong spelling of cooling scheme"
    print("Running...")
    sa = Simulated_annealing(
        state, temperature, 10000, valid_start_state=valid_start_state)
    sa.run(0, cooling_scheme)
    return sa.current_state


def run_plant_propagation(state: 'State', valid_start_state: bool) -> 'State':
    """
    runs a plant propagation algorithm and returns best state

    returns:
        State object
    """
    population_size: int = int(
        input("Pick a population size for plant propagation. (recommended: 10) "))
    max_generations: int = int(
        input("Choose a maximum number of generations. (recommended: 200) "))
    n_runners: int = int(
        input("Choose the number of runners. (recommended: 10) "))
    ppa = Plant_Propagation(state, valid_start_state,
                            population_size, max_generations, n_runners)
    ppa.run()
    return ppa.best_state


if __name__ == "__main__":

    #### ARGUMENT CHECKING ####
    # check if enough arguments are given
    if len(argv) < 3:
        print("usage: python main.py [case name] [algorithm]")
        exit()

    case_name: str = argv[1].lower()
    alg_name: str = argv[2].lower()

    # check if first argument is a valid case name
    if case_name != "holland" and case_name != "netherlands":
        print("usage: python main.py [holland|netherlands] [algorithm]")
        exit()

    # check if second algorithm is a valid algorithm name
    if alg_name not in ('hillclimber', 'hillclimber_restart', 'simulated_annealing', 'plant_propagation'):
        print(
            "usage: python main.py [case name] [baseline|hillclimber|hillclimber_restart|simulated_annealing|plant_propagation]")
        exit()

    state: 'State' = create_state(case_name)

    start_state: str = input(
        "Choose a start state for your algorithm [valid|random] (Valid can take very long for the Netherlands case): ")

    if start_state.lower() == "valid":
        valid_start_state = True
    elif start_state.lower() == "random":
        valid_start_state = False
    else:
        print("Start state should either be random or valid!")
        exit()

    # run chosen algorithm
    print(f"\nRunning {alg_name} algorithm. This may take a while.")
    if alg_name == "hillclimber":
        state = run_hillclimber(state, valid_start_state)
    elif alg_name == "hillclimber_restart":
        state = run_hillclimber_restart(state, valid_start_state)
    elif alg_name == "simulated_annealing":
        state = run_simulated_annealing(state, valid_start_state)
    elif alg_name == "plant_propagation":
        state = run_plant_propagation(state, valid_start_state)

    # show result state
    print("\nResult state:")
    print(state.show())

    # visualize result state
    print("\nLoading visualisation into your browser...")
    visualisation.show_plot(
        visualisation.get_station_info(state),
        state,
        case_name)
