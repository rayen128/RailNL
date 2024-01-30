from experiment_visualisation_functions import onegrid_hc, lines_comparison_long_experiments_hc, lines_comparison_long_experiments_ppa, onegrid_ppa
from results import read_csv

def make_plots_annealing():
    for case_name in ['holland', 'netherlands']:
        if case_name == 'holland':
            starts = ['valid', 'random']
        else:
            starts = ['random']
        for temperature in [100, 200, 500]:
            for cooling_scheme in ['exponential', 'logaritmic', 'lineair']:
                results_dict = read_csv(f"../../data/annealing/experiment_annealing_grid_search_{case_name}_{cooling_scheme}_{temperature}.csv", 'run_id')
                lines_comparison_long_experiments_hc(results_dict, f"../../docs/graphs/annealing/annealing_{temperature}_{cooling_scheme}_{case_name}", f"annealing {temperature} {cooling_scheme}")
                for start in starts:
                    for mutation in ["light", "heavy"]:
                        onegrid_hc(results_dict, f"../../docs/graphs/annealing/line_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}", f"Annealing {case_name} {cooling_scheme} {temperature} {start} {mutation}", start, mutation, 'linediagram')
                        onegrid_hc(results_dict, f"../../docs/graphs/annealing/histo_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}", f"Annealing {case_name} {cooling_scheme} {temperature} {start} {mutation}", start, mutation, 'histogram')

def make_plots_hill_climber():
    for algorithm in ['hill_climber', 'hill_climber_restart']:
        for case_name in ['holland', 'netherlands']:
            if case_name == 'holland':
                starts = ['valid', 'random']
            else:
                starts = ['random']
            results_dict = read_csv(f"../../data/{algorithm}/experiment_{algorithm}_grid_search_{case_name}.csv", 'run_id')
            lines_comparison_long_experiments_hc(results_dict, f"../../docs/graphs/{algorithm}/{algorithm}_{case_name}", f"{algorithm}", case_name)

            for start in starts:
                for mutation in ["light", "heavy"]:
                    onegrid_hc(results_dict, f"../../docs/graphs/{algorithm}/line_{algorithm}_{case_name}_{start}_{mutation}", f"{algorithm} holland {start} {mutation}", start, mutation, 'linediagram')
                    onegrid_hc(results_dict, f"../../docs/graphs/{algorithm}/histo_{algorithm}_{case_name}_{start}_{mutation}", f"{algorithm} holland {start} {mutation}", start, mutation, 'histogram')
                    
def make_plots_ppa(case_name: str, starting_states: str, filter_method: str):
    results_dict = read_csv(f"../../data/ppa/experiment_ppa_grid_search_{case_name}_{starting_states}_{filter_method}.csv", 'run_id')
    lines_comparison_long_experiments_ppa(results_dict, f"../../docs/graphs/ppa/{case_name}_{starting_states}_{filter_method}", f"ppa {case_name} {starting_states} {filter_method}", case_name)
    for population_size in [6, 12, 30]:
        for generation_count in [10, 50, 100]:
            for max_runners in [3, 7, 15]:
                onegrid_ppa(results_dict, f"../../docs/graphs/ppa/line_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}", f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'linediagram')
                onegrid_ppa(results_dict, f"../../docs/graphs/ppa/histo_{case_name}_{starting_states}_{filter_method}_{population_size}_{generation_count}_{max_runners}", f"ppa {case_name} {starting_states} {filter_method} {population_size} {generation_count} {max_runners}", population_size, generation_count, max_runners, 'histogram')

if __name__ == "__main__":
    make_plots_ppa('holland', 'hill_climber', 'sequential')