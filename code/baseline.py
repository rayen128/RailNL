import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 

def make_histogram(values: list, title_histogram: str) -> None:
    mean, std = norm.fit(values) 
    plt.hist(values, bins=50, density=True, edgecolor='black', color='#000066')

    xmin, xmax = plt.xlim() 
    linespace = np.linspace(xmin, xmax, 100) 
    line = norm.pdf(linespace, mean, std) 
    
    plt.plot(linespace, line, 'r', linewidth=2) 
    plt.title(title_histogram) 
    plt.savefig(f'../docs/histogram.png')

if __name__ == "__main__":
    x = np.random.normal(170, 10, 250)
    make_histogram(x, 'histogram')