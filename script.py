from code.scripts.experiment_plant_propagation import grid_search_PPA
from code.classes.state import State


# holland_state = State('data/stations_holland.csv',
#                       'data/routes_holland.csv', 7, 120)

# grid_search_PPA(state, 900, 'holland', 'hill_climber', 'sequential')

# grid_search_PPA(holland_state, 600, 'holland', 'random', 'sequential')


nl_state = State('data/stations_netherlands.csv',
                 'data/routes_netherlands.csv', 20, 180)

grid_search_PPA(nl_state, 900, 'netherlands', 'random', 'sequential')
grid_search_PPA(nl_state, 900, 'netherlands', 'hill_climber', 'sequential')
