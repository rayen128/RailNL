from experiment_visualisation_functions import onegrid_hc, lines_comparison_long_experiments_hc, lines_comparison_long_experiments_ppa, onegrid_ppa
from results import read_csv
import sys
import csv
csv.field_size_limit(sys.maxsize)


def make_plots_annealing():
    """
    makes all the plots for the annealing experiments

    pre:
        all the experiments are saved in a csv in a certain format

    post:
        created and saved all plots
    """
    # set right parameters
    for case_name in ['holland', 'netherlands']:
        if case_name == 'holland':
            starts = ['valid', 'random']
        else:
            starts = ['random']
        for temperature in [100, 200, 500]:
            for cooling_scheme in ['exponential', 'logaritmic', 'lineair']:

                # read csv with results
                results_dict = read_csv(
                    f"../../data/annealing/experiment_annealing_grid_search_{case_name}_{cooling_scheme}_{temperature}.csv", 'run_id')

                # make line diagram with different lines for best runs for every grid
                lines_comparison_long_experiments_hc(
                    results_dict, f"../../docs/graphs/annealing/2000/annealing_{temperature}_{cooling_scheme}_{case_name}", f"annealing {temperature} {cooling_scheme}", case_name)

                # create linediagram and histogram
                for start in starts:
                    for mutation in ["light", "heavy"]:
                        onegrid_hc(results_dict, f"../../docs/graphs/annealing/line_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}",
                                   f"Annealing {case_name} {cooling_scheme} {temperature} {start} {mutation}", start, mutation, 'linediagram')
                        onegrid_hc(results_dict, f"../../docs/graphs/annealing/histo_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}",
                                   f"Annealing {case_name} {cooling_scheme} {temperature} {start} {mutation}", start, mutation, 'histogram')


def make_plots_hill_climber():
    """
    makes all the plots for the hillclimber and hillclimber restart experiments

    pre:
        all the experiments are saved in a csv in a certain format

    post:
        created and saved all plots
    """

    # set parameters
    for algorithm in ['hill_climber', 'hill_climber_restart']:
        for case_name in ['holland', 'netherlands']:
            if case_name == 'holland':
                starts = ['valid', 'random']
            elif case_name == 'netherlands':
                starts = ['random']

            # create dict for results
            results_dict = read_csv(
                f"../../data/{algorithm}/experiment_{algorithm}_grid_search_{case_name}.csv", 'run_id')

            # create linediagram with different lines for every grid
            lines_comparison_long_experiments_hc(
                results_dict, f"../../docs/graphs/{algorithm}/{algorithm}_{case_name}", f"{algorithm}", case_name)

            # create linediagram and histogram for every plot
            for start in starts:
                for mutation in ["light", "heavy"]:
                    onegrid_hc(results_dict, f"../../docs/graphs/{algorithm}/line_{algorithm}_{case_name}_{start}_{mutation}",
                               f"{algorithm} {case_name} {start} {mutation}", start, mutation, 'linediagram')
                    onegrid_hc(results_dict, f"../../docs/graphs/{algorithm}/histo_{algorithm}_{case_name}_{start}_{mutation}",
                               f"{algorithm} {case_name} {start} {mutation}", start, mutation, 'histogram')


def make_plots_ppa_nl(case_name: str, starting_states: str, filter_method: str):
    """
    makes all the plots for the ppa netherlands experiments

    pre:
        all the experiments are saved in a csv in a certain format

    post:
        created and saved all plots
    """
    # save results in dict
    results_dict = read_csv(
        f"../../data/ppa/experiment_ppa_grid_search_{case_name}_{starting_states}_{filter_method}.csv", 'run_id')

    # create graph for every grid
    for population_size in [6, 30]:
        for generation_count in [200]:
            for max_runners in [3, 15]:
                for heuristic in [0, 1, 2]:
                    onegrid_ppa(results_dict, f"../../docs/graphs/ppa/line_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}_{heuristic}",
                                f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'linediagram', heuristic)
                    onegrid_ppa(results_dict, f"../../docs/graphs/ppa/histo_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}_{heuristic}",
                                f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'histogram', heuristic)


def make_plots_ppa(case_name: str, starting_states: str, filter_method: str):
    """
    makes all the plots for the ppa experiments

    pre:
        all the experiments are saved in a csv in a certain format

    post:
        created and saved all plots
    """

    # save results in dict
    results_dict = read_csv(
        f"../../data/ppa/experiment_ppa_grid_search_{case_name}_{starting_states}_{filter_method}.csv", 'run_id')

    # create line diagram with line for every grid
    lines_comparison_long_experiments_ppa(
        results_dict, f"../../docs/graphs/ppa/{case_name}_{starting_states}_{filter_method}", f"ppa {case_name} {starting_states} {filter_method}", case_name)

    # set parameters
    if filter_method == 'best' or filter_method == 'random' or (filter_method == 'sequential' and starting_states == 'random'):
        population_sizes = [12, 30]
        max_runners_list = [15, 7]
        generation_counters = [200]
    elif filter_method == 'sequential':
        population_sizes = [6, 12, 30]
        max_runners_list = [3, 7, 15]
        generation_counters = [10, 50, 100]

    # make graphs for every grid
    for population_size in population_sizes:
        for generation_count in generation_counters:
            for max_runners in max_runners_list:
                onegrid_ppa(results_dict, f"../../docs/graphs/ppa/line_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}",
                            f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'linediagram')
                onegrid_ppa(results_dict, f"../../docs/graphs/ppa/histo_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}",
                            f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'histogram')

