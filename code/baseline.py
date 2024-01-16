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

if __name__ == "__main__":
    x = np.random.normal(170, 10, 250)
    y = np.random.normal(170, 10, 250)
    p = np.random.normal(170, 10, 250)
    q = np.random.normal(170, 10, 250)
    
    #make_boxplot([x, y, p, q], 'boxplot')
    make_histogram(x, 'histogram')