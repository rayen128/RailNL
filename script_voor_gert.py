from code.scripts.experiment_plant_propagation import grid_search_PPA
from code.classes.state import State
from code.scripts.experiment_annealing_grid_search import *
from code.scripts.experiment_hill_climber_grid_search import *

nl_state = State('data/stations_netherlands.csv',
                 'data/routes_netherlands.csv', 20, 180)

# grid_search_PPA(nl_state, 3600, 'netherlands',
#                 'hill_climber_valid', 'sequential', specific=True)

# hill_climber random NL
# experiment_hill_climber_grid_search('netherlands', nl_state, 1800)

# valid states for NL:
# experiment_annealing_specific(
#     'netherlands_true', nl_state, 'valid', 1800, 'exponential', 200)


experiment_hill_climber_specific('netherlands_true', nl_state, 'valid', 1800)
