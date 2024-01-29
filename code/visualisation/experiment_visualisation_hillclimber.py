from results import *
from statistics import make_line_diagram_multiple_lines, make_histogram

def line_diagram_multiple_lines_hillclimber_onegrid_short_experiments(results_dict: dict, export_file_path: str, title_diagram: str, start: str, mutation: str):
    scores_lists = []
    filtered_results_start = filter_states(results_dict, 'start', start)
    filtered_results_mutation = filter_states(filtered_results_start, 'mutation', mutation)
    
    key_first_run = list(filtered_results_mutation.keys())[0]
    first_run = filtered_results_mutation[key_first_run]['run_id']

    key_last_run = list(filtered_results_mutation.keys())[-1]
    last_run = filtered_results_mutation[key_last_run]['run_id']

    for run in range(int(first_run), int(last_run) + 1):
        filtered_results = filter_states(results_dict, 'run_id', str(run))
        scores_run = all_scores(filtered_results)
        scores_lists.append(scores_run)

    make_line_diagram_multiple_lines(scores_lists, title_diagram, export_file_path, False)

def line_diagram_multiple_lines_hillclimber_comparison_short_experiments(results_dict: dict, export_file_path: str, title_diagram: str):
    best_scores_lists = []
    start_parameters = ['valid', 'random']
    mutation_parameters = ['light', 'heavy']
    
    for start in start_parameters:
        filtered_results_start = filter_states(results_dict, 'start', start)
        for mutation in mutation_parameters:
            filtered_results = filter_states(filtered_results_start, 'mutation', mutation)
            sorted_results = dict(sorted(filtered_results.items(), key=lambda x: float(x[1]['score']), reverse=True))
            key_run = list(sorted_results.keys())[0]
            run =  str(filtered_results[key_run]['run_id'])
            run_results = filter_states(filtered_results, 'run_id', run)
            scores_run = all_scores(run_results)
            best_scores_lists.append(scores_run)
            
    make_line_diagram_multiple_lines(best_scores_lists, title_diagram, export_file_path, True)

def histogram_hillclimber_onegrid(results_dict: dict, export_file_path: str, title_diagram: str, start: str, mutation: str):
    end_scores_list = []
    filtered_results_start = filter_states(results_dict, 'start', start)
    filtered_results_mutation = filter_states(filtered_results_start, 'mutation', mutation)
    
    key_first_run = list(filtered_results_mutation.keys())[0]
    first_run = filtered_results_mutation[key_first_run]['run_id']

    key_last_run = list(filtered_results_mutation.keys())[-1]
    last_run = filtered_results_mutation[key_last_run]['run_id']

    for run in range(int(first_run), int(last_run) + 1):
        filtered_results = filter_states(results_dict, 'run_id', str(run))
        scores_run = all_scores(filtered_results)
        end_scores_list.append(scores_run[-1])

    make_histogram(end_scores_list, title_diagram, export_file_path)

def line_diagram_multiple_lines_hillclimber_onegrid_long_experiments(results_dict: dict, export_file_path: str, title_diagram: str, start: str, mutation: str):
    scores_lists = []
    filtered_results_start = filter_states(results_dict, 'start', start)
    filtered_results_mutation = filter_states(filtered_results_start, 'mutation', mutation)

    for run in filtered_results_mutation.values():
        scores_lists.append(str_to_list(run['score_list']))
        

    make_line_diagram_multiple_lines(scores_lists, title_diagram, export_file_path, False)

def line_diagram_multiple_lines_hillclimber_comparison_long_experiments(results_dict: dict, export_file_path: str, title_diagram: str):
    best_scores_lists = []
    legend = []
    start_parameters = ['valid', 'random']
    mutation_parameters = ['light', 'heavy']
    
    for start in start_parameters:
        filtered_results_start = filter_states(results_dict, 'start', start)
        for mutation in mutation_parameters:
            filtered_results = filter_states(filtered_results_start, 'mutation', mutation)
            sorted_results = dict(sorted(filtered_results.items(), key=lambda x: float(x[1]['score']), reverse=True))
            key_run = list(sorted_results.keys())[0]
            best_scores = str_to_list(filtered_results[key_run]['score_list'])
            best_scores_lists.append(best_scores)
            legend.append(f"{start}, {mutation}")
            
    make_line_diagram_multiple_lines(best_scores_lists, title_diagram, export_file_path, True, legend)





if __name__ == "__main__":
    results_dict = read_csv("../../data/hill_climber/experiment_hill_climber_grid_search_holland.csv", 'run_id')
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber_restart/experiment_hill_climber_restart_grid_search_holland.csv", "hill_climber_restart_valid_light", "test line diagram experiment", "valid", "light")
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber_restart/experiment_hill_climber_restart_grid_search_holland.csv", "hill_climber_restart_valid_heavy", "test line diagram experiment", "valid", "heavy")
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber_restart/experiment_hill_climber_restart_grid_search_holland.csv", "hill_climber_restart_random_light", "test line diagram experiment", "random", "light")
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber_restart/experiment_hill_climber_restart_grid_search_holland.csv", "hill_climber_restart_random_heavy", "test line diagram experiment", "random", "heavy")
    
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber/experiment_hill_climber_grid_search_holland.csv", "hill_climber_valid_light", "test line diagram experiment", "valid", "light")
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber/experiment_hill_climber_grid_search_holland.csv", "hill_climber_valid_heavy", "test line diagram experiment", "valid", "heavy")
    #line_diagram_multiple_lines_hillclimber_onegrid_short_experiments("../../data/hill_climber/experiment_hill_climber_grid_search_holland.csv", "hill_climber_random_light", "test line diagram experiment", "random", "light")
    line_diagram_multiple_lines_hillclimber_comparison_long_experiments(results_dict, "hill_climber_random_heavy", "test line diagram experiment")
    
    
    #histogram_hillclimber_onegrid(results_dict, "hill_climber", "test histogram experiment", "valid", "light")