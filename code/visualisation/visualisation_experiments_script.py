from experiment_visualisation_functions import histogram_onegrid, lines_onegrid_long_experiments, lines_comparison_long_experiments
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
                lines_comparison_long_experiments(results_dict, f"../../docs/graphs/annealing/annealing_{temperature}_{cooling_scheme}_{case_name}", f"annealing {temperature} {cooling_scheme}")
                for start in starts:
                    for mutation in ["light", "heavy"]:
                        lines_onegrid_long_experiments(results_dict, f"../../docs/graphs/annealing/line_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}", f"Annealing holland {cooling_scheme} {temperature} {start} {mutation}", start, mutation)
                        histogram_onegrid(results_dict, f"../../docs/graphs/annealing/histo_annealing_{case_name}_{cooling_scheme}_{temperature}_{start}_{mutation}" f"Annealing holland {cooling_scheme} {temperature} {start} {mutation}", start, mutation)
                

def make_plots_hill_climber():
    for algorithm in ['hill_climber', 'hill_climber_restart']:
        for case_name in ['holland', 'netherlands']:
            if case_name == 'holland':
                starts = ['valid', 'random']
            else:
                starts = ['random']
            results_dict = read_csv(f"../../data/{algorithm}/experiment_{algorithm}_grid_search_{case_name}.csv", 'run_id')
            lines_comparison_long_experiments(results_dict, f"../../docs/graphs/{algorithm}/{algorithm}_{case_name}", f"{algorithm}", case_name)

            for start in starts:
                for mutation in ["light", "heavy"]:
                    lines_onegrid_long_experiments(results_dict, f"../../docs/graphs/{algorithm}/line_{algorithm}_{case_name}_{start}_{mutation}", f"{algorithm} holland {start} {mutation}", start, mutation)
                    histogram_onegrid(results_dict, f"../../docs/graphs/{algorithm}/histo_{algorithm}_{case_name}_{start}_{mutation}", f"{algorithm} holland {start} {mutation}", start, mutation)

if __name__ == "__main__":
    make_plots_hill_climber()