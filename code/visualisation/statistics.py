import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import islice
import statistics

from results import read_csv, filter_states, all_scores, export_states

def make_histogram(values: list, title_histogram: str, filepath: str) -> None:
    """
    creates and saves a histogram with normal distribution line with the given values

    pre:
        values is a list with values
        title_histogram and filepath are strings

    post:
        a png file is saved with a histogram
    """
    plt.clf()

    # make the histogram
    plt.hist(values, bins=50, density=True, edgecolor='black', color='#000066')

    # set the normal distribution line
    mean, std = norm.fit(values)
    xmin, xmax = plt.xlim()
    linespace = np.linspace(xmin, xmax, 100)
    line = norm.pdf(linespace, mean, std)

    # create and save plot
    plt.plot(linespace, line, 'r', linewidth=2)
    plt.title(title_histogram)
    plt.xlabel("scores", labelpad=10)
    plt.ylabel("relative frequency", labelpad=10)
    plt.subplots_adjust(left=0.17, right=0.9, top=0.9, bottom=0.15)
    plt.savefig(
        f'{filepath}.png')


def make_boxplot(values: list, title_boxplot: str, filepath: str, legend: list[str]) -> None:
    """
    makes a boxplot for all algorithms and the total scores 

    pre:
        values is a list with 4 lists of values inside
        title and filepath are strings

    post:
        a png file is saved with the plot
    """

    # code from GeeksforGeeks
    # make plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # creating axes instance
    bp = ax.boxplot(values, patch_artist=True, vert=False)

    # set colors subplots
    colors = ['#5e747f', '#7b9e87',
              '#6b2737', '#f5e7e0']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # Adding title
    plt.title(f"{title_boxplot}")
    plt.xlabel("Scores")
    plt.ylabel("Algorithms")

    # set x-axis labels
    ax.set_yticklabels(legend)

    # save the plot in a png
    plt.savefig(
        f'{filepath}.png')
    
def make_line_diagram(scores: list, title_diagram: str, filepath: str) -> None:
    """
    makes a line diagram of the scores against the iterations

    pre:
        the scores in the list is in the same order as the amount of iterations
        scores is a list with integers
        title_diagram and filepath are strings

    post:
        saves a png file with the line diagram
    """
    plt.clf()
    
    x = list(range(len(scores)))
    
    plt.plot(x, scores)
    plt.xlabel("Iterations")
    plt.ylabel("Scores")
    plt.title(f"{title_diagram}")
    plt.savefig(
        f'{filepath}.png')
    
def make_line_diagram_multiple_lines(scores: list[list], title_diagram: str, filepath: str, comparison: bool, legend: list[str] = None) -> None:
    """
    makes a line diagram with multiple lines of the scores against the iterations

    pre:
        the scores in the list is in the same order as the amount of iterations
        scores is a list with integers
        title_diagram and filepath are strings

    post:
        saves a png file with the line diagram
    """
    plt.clf()
    
    for i in range(len(scores)):
        x = list(range(len(scores[i])))
        if not comparison:
            plt.plot(x, scores[i], alpha=0.2, color='magenta')
        else:
            plt.plot(x, scores[i])

    plt.legend(legend, loc = "lower right")
    plt.xlabel("Iterations")
    plt.ylabel("Scores")
    plt.title(f"{title_diagram}")
    plt.savefig(
        f'{filepath}.png')
    
def ranking(states_dict: dict, amount: int):
    """
    prints a ranking with the states with the highest scores

    pre:
        states_dict is a dict with which maintains state dictionaries
        solved is a boolean which indicates if the user only wants to rank the valid solutions
        amount is a int which indicates how much states the user wants to rank

    post:
        prints a ranking with the top states with all the information

    """

    # sort the states dictionary based on scores
    sorted_states = dict(
        sorted(states_dict.items(), key=lambda x: float(x[1]['score']), reverse=True))
    
    # print the column names
    print("state id \t algorithm \t \t \t score\t\t\tused connections \t routes \ttotal minutes \tis solution")

    # print the states
    for state in islice(sorted_states.values(), amount):
        print(f"{state['state_id']} \t \t {state['algorithm']} \t \t {state['score']} \t \t"
                f"{state['fraction_used_connections']} \t \t \t {state['number_routes']} \t \t"
                f"{state['total_minutes']} \t \t{state['is_solution']}")
            

def statistics_scores(scores: list) -> dict:
    """
    calculates all the important statistics

    pre:
        scores is a list with scores

    returns:
        a dictionary with all the important statistics
    """

    # add statistics to dictionary
    statistics_scores_dict = {} 
    statistics_scores_dict['min_score'] = min(scores)
    statistics_scores_dict['max_score'] = max(scores)
    statistics_scores_dict['mean'] = sum(scores) / len(scores)
    statistics_scores_dict['stdev'] = statistics.stdev(scores)

    return statistics_scores_dict

if __name__ == "__main__":

    states_results = read_csv("../../data/baseline_data_holland.csv", "state_id")
    filtered_results_1 = filter_states(states_results, 'algorithm', 'random_algorithm_2')
    scores_1 = all_scores(filtered_results_1)

    filtered_results_2 = filter_states(states_results, 'algorithm', 'random_algorithm_2')
    scores_2 = all_scores(filtered_results_2)
    
    filtered_results_3 = filter_states(states_results, 'algorithm', 'random_algorithm_3')
    scores_3 = all_scores(filtered_results_3)

    scores_total = all_scores(states_results)
    scores = [scores_1, scores_2, scores_3, scores_total]
    make_boxplot(scores, 'Boxplot Baseline', 'boxplot', ['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Total'])
