import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 

def make_histogram(values: list, title_histogram: str) -> None:
    """
    creates and saves a histogram with normal distribution line with the given values

    pre:
        values is a list with values
        title_histogram is a string

    post:
        a png file is saved with a histogram
    """
    
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
    plt.savefig(f'../docs/{title_histogram}.png')

def make_boxplot(values: list, title_boxplot: str) -> None:
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
    bp = ax.boxplot(values, patch_artist = True, notch ='True', vert = True)

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
    plt.savefig(f'../docs/{title_boxplot}.png')

def read_csv(csv_filepath: str) -> dict:
    states_dict: dict = {}
    
    with open(csv_filepath) as states:
        csv_reader = csv.DictReader(states)
        for row in csv_reader:
            states_dict[row["station"]] = row

    ranking(states_dict, True, 8)

"""
def all_scores(states_dict: dict) -> list:
    scores = []

    for state in states_dict:
        scores.append(state[score])

    return scores

def scores_algorithm(states_dict: dict, algorithm: str) -> list:
    scores = []

    for state in states_dict:
        if states_dict['algorithm'] == algorithm:
            scores.append(state[score])
    
    return scores
"""

def ranking(states_dict: dict, solved: bool, amount: int):
    sorted_states = sorted(states_dict.items()["x"], key=lambda x:x[1])
    print(sorted_states)





if __name__ == "__main__":
    x = np.random.normal(170, 10, 250)
    y = np.random.normal(170, 10, 250)
    p = np.random.normal(170, 10, 250)
    q = np.random.normal(170, 10, 250)
    
    #make_boxplot([x, y, p, q], 'boxplot')
    #make_histogram(x, 'histogram')
    read_csv("../data/stations_holland.csv")
