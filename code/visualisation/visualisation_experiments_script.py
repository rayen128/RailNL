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


if __name__ == "__main__":
    from results import filter_states, all_scores, str_to_list
    from statistics import make_line_diagram_multiple_lines, make_histogram

    # make_plots_ppa_nl('netherlands', 'hill_climber', 'sequential')

    #results_dict = read_csv(f"../../data/annealing/experiment_annealing_grid_search_netherlands_logaritmic_200.csv", 'run_id')
    #onegrid_hc(results_dict, f"../../docs/presentation/assets/plots_def/line_annealing_netherlands_logaritmic_200_valid_heavy", "Simulated annealing Netherlands logarithmic 200 valid heavy", "valid", "heavy", 'linediagram')
    """
    best_scores_lists = []
    legend = []

    results_dict_logaritmic = read_csv(f"../../data/annealing/experiment_annealing_grid_search_holland_logaritmic_200.csv", 'run_id')
    results_dict_lineair = read_csv(f"../../data/annealing/experiment_annealing_grid_search_holland_lineair_200.csv", 'run_id')
    results_dict_exponential = read_csv(f"../../data/annealing/experiment_annealing_grid_search_holland_exponential_200.csv", 'run_id')
    
    
    # sort results
    sorted_results = dict(sorted(results_dict_logaritmic.items(), key=lambda x: float(x[1]['score']), reverse=True))

    # get results of the best run
    key_run = list(sorted_results.keys())[0]
    best_scores = str_to_list(results_dict_logaritmic[key_run]['score_list'])
    best_scores_lists.append(best_scores)

    # save legend values
    legend.append("Logarithmic")

    # sort results
    sorted_results = dict(sorted(results_dict_lineair.items(), key=lambda x: float(x[1]['score']), reverse=True))

    # get results of the best run
    key_run = list(sorted_results.keys())[0]
    best_scores = str_to_list(results_dict_lineair[key_run]['score_list'])
    best_scores_lists.append(best_scores)

    # save legend values
    legend.append("Linear")

    # sort results
    sorted_results = dict(sorted(results_dict_exponential.items(), key=lambda x: float(x[1]['score']), reverse=True))

    # get results of the best run
    key_run = list(sorted_results.keys())[0]
    best_scores = str_to_list(results_dict_exponential[key_run]['score_list'])
    best_scores_lists.append(best_scores)

    # save legend values
    legend.append("Exponential")

    make_line_diagram_multiple_lines(best_scores_lists, "Simulated Annealing comparison cooling schemes 200", "../../docs/presentation/assets/plots_def/comparison_annealing_holland_200", True, None, legend)
    """




    #make_plots_hill_climber()
    #make_plots_annealing()
    #make_plots_ppa('netherlands', 'hill_climber', 'random')
    #make_plots_ppa('netherlands', 'hill_climber', 'best')
    #make_plots_ppa('holland', 'random', 'sequential')
    #make_plots_ppa_nl('netherlands', 'hill_climber', 'sequential')

    results_dict_lineair = read_csv(f"../../data/annealing/experiment_annealing_grid_search_netherlands_lineair_200.csv", 'run_id')
    results_dict_logaritmic = read_csv(f"../../data/annealing/experiment_annealing_grid_search_netherlands_logaritmic_200.csv", 'run_id')
    results_dict_exponential = read_csv(f"../../data/annealing/experiment_annealing_grid_search_netherlands_exponential_200.csv", 'run_id')
    #onegrid_hc(results_dict, f"../../docs/presentation/assets/plots_def/line_annealing_netherlands_logaritmic_200_valid_heavy", "Simulated annealing Netherlands logarithmic 200 valid heavy", "valid", "heavy", 'linediagram')



    #onegrid_hc(results_dict, f"../../docs/presentation/assets/plots_def/histo_hill_climber_holland_valid_heavy", "Hill-climber Holland valid heavy", "valid", "heavy", 'histogram')
    #onegrid_hc(results_dict, f"../../docs/presentation/assets/plots_def/histo_hill_climber_holland_random_heavy", "Hill-climber Holland random heavy", "random", "heavy", 'histogram')
    onegrid_hc(results_dict_lineair, f"../../docs/presentation/assets/plots_def/histo_annealing_netherlands_lineair_200_random_heavy", "Simulated annealing Netherlands linear 200 random", "random", "heavy", 'histogram')
    onegrid_hc(results_dict_logaritmic, f"../../docs/presentation/assets/plots_def/histo_annealing_netherlands_logaritmic_200_random_heavy", "Simulated annealing Netherlands logarithmic 200 random", "random", "heavy", 'histogram')
    onegrid_hc(results_dict_exponential, f"../../docs/presentation/assets/plots_def/histo_annealing_netherlands_exponential_200_random_heavy", "Simulated annealing Netherlands exponential 200 random", "random", "heavy", 'histogram')