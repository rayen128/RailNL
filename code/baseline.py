import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import islice
import statistics


def make_histogram(values: list, title_histogram: str, area: str) -> None:
    """
    creates and saves a histogram with normal distribution line with the given values

    pre:
        values is a list with values
        title_histogram is a string

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
    filename = title_histogram.replace(" ", "_").lower()
    plt.savefig(
        f'../docs/assignments/baseline/figures_baseline_{area}/{filename}.png')


def make_boxplot(values: list, title_boxplot: str, area: str) -> None:
    """
    makes a boxplot for all algorithms and the total scores 

    pre:
        values is a list with 4 lists of values inside
        title is a string

    post:
        a png file is saved with the plot
    """

    # code from GeeksforGeeks
    # make plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # creating axes instance
    bp = ax.boxplot(values, patch_artist=True, vert=True)

    # set colors subplots
    colors = ['#5e747f', '#7b9e87',
              '#6b2737', '#f5e7e0']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # Adding title
    plt.title(f"{title_boxplot}")

    # set x-axis labels
    ax.set_xticklabels(['algoritme 1', 'algoritme 2',
                        'algoritme 3', 'totaal'])

    # save the plot in a png
    filename = title_boxplot.replace(" ", "_").lower()
    plt.savefig(
        f'../docs/assignments/baseline/figures_baseline_{area}/{filename}.png')


def read_csv(csv_filepath: str) -> dict:
    """
    reads csv file with states and saves every state in a dictionary
    saves a dictionary with all the states dictionaries with state id as key

    pre: 
        csv_filepath is a string with a excisting csv file

    post:
        makes a dictionary with all the states in dictionaries

    returns:
        the dictionary with all the states

    """
    # make dictionary for saving the states
    states_dict: dict = {}

    # add every row to the dictionary with state id as key
    with open(csv_filepath) as states:
        csv_reader = csv.DictReader(states)
        for row in csv_reader:
            states_dict[row["state_id"]] = row

    return states_dict


def all_scores(states_dict: dict) -> list:
    """
    makes a list with all the scores from every state

    pre: 
        states_dict is a dict with which maintains state dictionaries  

    returns:
        the list with scores
    """

    # make an empty list to save the scores into
    scores = []

    # add all the scores from every state to the list
    for state in states_dict.values():
        scores.append(int(round(float(state["score"]), 0)))

    return scores


def scores_algorithm(states_dict: dict, algorithm: str) -> list:
    """
    makes a list with all the scores from the states from a certain algorithm

    pre: 
        states_dict is a dict with which maintains state dictionaries  

    returns:
        the list with scores
    """
    # make an empty list to save the scores into
    scores = []

    # add the score to the list from the states with the given algorithm
    for state in states_dict.values():
        if state['algorithm'] == algorithm:
            scores.append(int(round(float(state['score']), 0)))

    return scores


def ranking(states_dict: dict, solved: bool, algorithm: str | None, amount: int):
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
    print("state id \t algorithm \t \t \t score\t\t\tused connections \t routes \ttotal minutes")

    # print the states
    for state in islice(sorted_states.values(), amount):
        if (not solved or (solved and state['is_solution'] == 'True')) or (algorithm and state['algorithm'] == algorithm):
            print(f"{state['state_id']} \t \t {state['algorithm']} \t \t {state['score']} \t \t"
                  f"{state['fraction_used_connections']} \t \t \t {state['number_routes']} \t \t"
                  f"{state['total_minutes']} \t \t")


def statistics_scores(scores: list) -> dict:
    """
    calculates all the important statistics

    pre:
        scores is a list with scores

    returns:
        a dictionary with all the important statistics
    """

    # calculate all statistics
    min_score = min(scores)
    max_score = max(scores)
    mean = sum(scores) / len(scores)
    stdev = statistics.stdev(scores)

    statistics_scores_dict = {}
    statistics_scores_dict['min_score'] = min_score
    statistics_scores_dict['max_score'] = max_score
    statistics_scores_dict['mean'] = mean
    statistics_scores_dict['stdev'] = stdev

    return statistics_scores_dict


if __name__ == "__main__":

    states_results = read_csv("../data/baseline_data_holland.csv")

    total_scores = all_scores(states_results)
    scores_algorithm_1 = scores_algorithm(states_results, 'random_algorithm_1')

    make_histogram(
        total_scores, 'Scores van alle algoritmes Holland', 'holland')

    make_histogram(scores_algorithm_1,
                   'Scores van algoritme 1 Holland', 'holland')
    scores_algorithm_2 = scores_algorithm(states_results, 'random_algorithm_2')
    make_histogram(scores_algorithm_2,
                   'Scores van algoritme 2 Holland', 'holland')
    scores_algorithm_3 = scores_algorithm(states_results, 'random_algorithm_3')
    make_histogram(scores_algorithm_3,
                   'Scores van algoritme 3 Holland', 'holland')
    make_boxplot([scores_algorithm_1, scores_algorithm_2,
                 scores_algorithm_3, total_scores], 'Boxplot', 'holland')
    # ranking(states_results, False, 20)
    # stats_total, stats_1, stats_2, stats_3 = statistics_scores(total_scores), \
    # statistics_scores(scores_algorithm_1), statistics_scores(scores_algorithm_2), \
    # statistics_scores(scores_algorithm_3)

    # print(f"statistics total: {stats_total} \nstatistics 1: {stats_1} \n"
    # f"statistics 2: {stats_2} \nstatistics 3: {stats_3}")

    # states_results = read_csv("../data/baseline_data_netherlands.csv")
    # total_scores = all_scores(states_results)
    # make_histogram(total_scores, 'Scores van alle algoritmes Netherlands', 'netherlands')
    # scores_algorithm_1 = scores_algorithm(states_results, 'random_algorithm_1')
    # make_histogram(scores_algorithm_1, 'Scores van algoritme 1 Netherlands', 'netherlands')
    # scores_algorithm_2 = scores_algorithm(states_results, 'random_algorithm_2')
    # make_histogram(scores_algorithm_2, 'Scores van algoritme 2 Netherlands', 'netherlands')
    # scores_algorithm_3 = scores_algorithm(states_results, 'random_algorithm_3')
    # make_histogram(scores_algorithm_3, 'Scores van algoritme 3 Netherlands', 'netherlands')
    # make_boxplot([scores_algorithm_1, scores_algorithm_2,
    # scores_algorithm_3, total_scores], 'Boxplot Netherlands')
