from code.scripts.experiment_plant_propagation import grid_search_PPA_hill_climber, experiment_best_filter, experiment_long_ppa
from code.classes.state import State


state = State('data/stations_netherlands.csv', 'data/routes_netherlands.csv', 20, 180)
experiment_best_filter(state, 900, 'netherlands', 'hill_climber')
experiment_long_ppa((state, 'netherlands', 'hill_climber', 'sequential'))