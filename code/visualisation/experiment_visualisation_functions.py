from results import filter_states, all_scores, str_to_list
from statistics import make_line_diagram_multiple_lines, make_histogram

def lines_onegrid_short_experiments(results_dict: dict, export_file_path: str, title_diagram: str, start: str, mutation: str) -> None:
    """
    makes line diagram with multiple lines for one grid for the experiments with the csv files with a line for every iteration

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram, start and mutation are strings
    
    post:
        makes line diagram with multiple lines for every run in a certain grid
    """
    
    # get filtered results
    filtered_results_start = filter_states(results_dict, 'start', start)
    filtered_results_mutation = filter_states(filtered_results_start, 'mutation', mutation)
    
    # get iterations from grid
    key_first_run = list(filtered_results_mutation.keys())[0]
    first_run = filtered_results_mutation[key_first_run]['run_id']

    key_last_run = list(filtered_results_mutation.keys())[-1]
    last_run = filtered_results_mutation[key_last_run]['run_id']

    # make a list with lists in it with all scores for that grid
    scores_lists = []

    for run in range(int(first_run), int(last_run) + 1):
        filtered_results = filter_states(results_dict, 'run_id', str(run))
        scores_run = all_scores(filtered_results)
        scores_lists.append(scores_run)

    make_line_diagram_multiple_lines(scores_lists, title_diagram, export_file_path, False)

def lines_comparison_short_experiments(results_dict: dict, export_file_path: str, title_diagram: str) -> None:
    """
    plots the best line for every grid for the experiments with the csv files with a line for every iteration

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram are strings

    post:
        a line diagram with several lines is created
    
    """
    # create an empty list to collect all the lists with scores
    best_scores_lists = []
    
    # get the results for every grid
    for start in ['valid', 'random']:
        filtered_results_start = filter_states(results_dict, 'start', start)
        for mutation in ['light', 'heavy']:
            filtered_results = filter_states(filtered_results_start, 'mutation', mutation)
            
            # sort the results based on score
            sorted_results = dict(sorted(filtered_results.items(), key=lambda x: float(x[1]['score']), reverse=True))
            
            # get the scores for the best run
            key_run = list(sorted_results.keys())[0]
            run = str(filtered_results[key_run]['run_id'])
            run_results = filter_states(filtered_results, 'run_id', run)
            scores_run = all_scores(run_results)

            # add the scores to the list with scores
            best_scores_lists.append(scores_run)

    # plot diagram      
    make_line_diagram_multiple_lines(best_scores_lists, title_diagram, export_file_path, True)

def lines_comparison_long_experiments_hc(results_dict: dict, export_file_path: str, title_diagram: str, case_name: str) -> None:
    """
    plots the best line for every grid for the experiments with the csv files with more runs

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram are strings

    post:
        a line diagram with several lines is created
    
    """
    # create an empty list to collect all lists with the scores
    best_scores_lists = []

    # create an empty list to collect the legens values
    legend = []

    # get the right parameters for every case
    if case_name == 'holland':
        start_parameters = ['valid', 'random']
    else:
        start_parameters = ['random']
    
    # filter the results for the right grid
    for start in start_parameters:
        filtered_results_start = filter_states(results_dict, 'start', start)
        for mutation in ['light', 'heavy']:
            filtered_results = filter_states(filtered_results_start, 'mutation', mutation)

            # sort results
            sorted_results = dict(sorted(filtered_results.items(), key=lambda x: float(x[1]['score']), reverse=True))

            # get results of the best run
            key_run = list(sorted_results.keys())[0]
            best_scores = str_to_list(filtered_results[key_run]['score_list'])
            best_scores_lists.append(best_scores)

            # save legend values
            legend.append(f"{start}, {mutation}")

    # plot diagram       
    make_line_diagram_multiple_lines(best_scores_lists, title_diagram, export_file_path, True, None, legend)

def lines_comparison_long_experiments_ppa(results_dict: dict, export_file_path: str, title_diagram: str, case_name: str) -> None:
    """
    plots the best line for every grid for the experiments with the csv files with more runs

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram are strings

    post:
        a line diagram with several lines is created
    
    """
    
    # create an empty list to collect all lists with the scores
    best_scores_lists = []

    # create an empty list to collect the legens values
    legend = []

    # get the right parameters for every case
    if case_name == 'holland':
        population_sizes = [6, 12, 30]
        generation_counters = [10, 50, 100]
        max_runners = [3, 7, 15]
    elif case_name == 'netherlands':
        population_sizes = [12, 30]
        generation_counters = [200]
        max_runners = [3, 15]
    
    # filter the results for the right grid
    for population_size in population_sizes:
        filtered_results_population = filter_states(results_dict, 'population_size', str(population_size))
        for generation_count in generation_counters:
            filtered_results_generation = filter_states(filtered_results_population, 'generation_count', str(generation_count))
            for max_runner in max_runners:
                filtered_results = filter_states(filtered_results_generation, 'max_runners', str(max_runner))
                
                # sort results
                sorted_results = dict(sorted(filtered_results.items(), key=lambda x: float(x[1]['score']), reverse=True))
                
                 # get results of the best run
                if sorted_results != {}:
                    key_run = list(sorted_results.keys())[0]
                    best_scores = str_to_list(filtered_results[key_run]['score_list'])
                    best_scores_lists.append(best_scores)

                # save legend values
                legend.append(f"Population-size:{population_size}, generation-count:{generation_count}, max-runners:{max_runner}")

    # plot diagram    
    make_line_diagram_multiple_lines(best_scores_lists, title_diagram, export_file_path, True, None, legend)

def onegrid_hc(results_dict: dict, export_file_path: str, title_diagram: str, start: str, mutation: str, plot: str) -> None:
    """
    filters the results for the right grid for the hillclimber and annealing experiments

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram, start, mutation and plot are strings
    
    post:
        gives the results to a function to make the plot

    """             
    # filter results
    filtered_results_start = filter_states(results_dict, 'start', start)
    filtered_results_mutation = filter_states(filtered_results_start, 'mutation', mutation)
    
    # plot the right plot
    if plot == 'histogram':
        histogram_onegrid(results_dict, filtered_results_mutation, title_diagram, export_file_path)
    elif plot == 'linediagram':
        lines_onegrid_long_experiments(filtered_results_mutation, export_file_path, title_diagram)


def onegrid_ppa(results_dict: dict, export_file_path: str, title_diagram: str, population_size: int, generation_count: int, max_runners: int, plot: str, heuristic_value: int = None) -> None:
    """
    filters the results for the right grid for the ppa experiments

    pre:
        results_dict is a dictionary with dictionaries for every iteration
        export_file_path, title_diagram, start, mutation and plot are strings
    
    post:
        gives the results to the function to make a plot

    """
    
    # filter the results
    filtered_results_population_size = filter_states(results_dict, 'population_size', str(population_size))
    filtered_results_generation = filter_states(filtered_results_population_size, 'generation_count', str(generation_count))
    filtered_results = filter_states(filtered_results_generation, 'max_runners', str(max_runners))
    if heuristic_value:
        filtered_results = filter_states(filtered_results, 'heuristic_value', str(heuristic_value))

    # plot the right plot
    if plot == 'histogram' and filtered_results != {}:
        histogram_onegrid(results_dict, filtered_results, title_diagram, export_file_path)
    elif plot == 'linediagram' and filtered_results != {}:
        lines_onegrid_long_experiments(filtered_results, export_file_path, title_diagram, 'Generations')

    
def histogram_onegrid(results_dict: dict, filtered_results: dict, title_diagram: str, export_file_path: str) -> None:
    """
    makes histogram for a certain grid

    pre:
        results_dict and filtered_results are dictionaries with dictionaries for every iteration
        export_file_path and title_diagram are strings
    
    post:
        plots a histogram

    """
    
    # create empty list for all score-lists
    end_scores_list = []
    
    # get the first and last run id
    
    key_first_run = list(filtered_results.keys())[0]
    first_run = filtered_results[key_first_run]['run_id']

    key_last_run = list(filtered_results.keys())[-1]
    last_run = filtered_results[key_last_run]['run_id']

    runs = int(key_last_run) - int(key_first_run)

    # save the endscores of every run in the grid
    for run in range(int(first_run), int(last_run) + 1):
        filtered_results_run = filter_states(results_dict, 'run_id', str(run))
        scores_run = all_scores(filtered_results_run)
        end_scores_list.append(scores_run[-1])

    # plot histogram
    make_histogram(end_scores_list, title_diagram, export_file_path, f'runs: {runs}')

def lines_onegrid_long_experiments(filtered_results: dict, export_file_path: str, title_diagram: str, xlabel: str = 'Iterations'):
    """
    makes linediagram for a certain grid with lines for every run

    pre:
        results_dict and filtered_results are dictionaries with dictionaries for every iteration
        export_file_path and title_diagram are strings
    
    post:
        plots a linediagram

    """
    # create empty for every score list
    scores_lists = []
    runs = 0
    
    # collect all scores for grid
    for run in filtered_results.values():
        score_list = str_to_list(run['score_list'])
        scores_lists.append(score_list)
        runs += 1
    
    # plot diagram
    make_line_diagram_multiple_lines(scores_lists, title_diagram, export_file_path, False, f'runs: {runs}', None, xlabel)
