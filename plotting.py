from parse import *

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

COLORS = ["#D0D1E6", "#A6BDDB", "#74A9CF", "#2B8CBE", "#045A8D"]


def gaussian_smooth(x, y, grid, sd):
    weights = np.transpose([stats.norm.pdf(grid, m, sd) for m in x])
    weights = weights / weights.sum(0)
    return (weights * y).sum(1)


def plot(x,gauss = True):

    fig, ax = plt.subplots(figsize=(10, 7))
    ndata = len(x)
    
    if gauss:
        grid = np.linspace(0, ndata, num=1000)
        y_smoothed = [gaussian_smooth(list(range(ndata)), y_, grid, .5) for y_ in x.values.T]
        
    else:
        grid=list(range(ndata))
        y_smoothed = x.values.T
    ax.stackplot(grid, y_smoothed, colors=COLORS, baseline="sym")

    # print(x)
   
    # labels
    
    
    fig.set_size_inches(.3*len(x), 6)
    # plt.scatter(x, y, c=x, s=500, cmap='RdYlGn', alpha=0.8)

    labels = ['' for item in ax.get_xticklabels()]
    

    ax.set_xticklabels(labels)
        
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    if not gauss:
        w = 0.55


    else:
        w = x.max(axis=1).max()
    for j,s in enumerate(chapters):
        ax.text(j, w, ''+s , size = 'x-small', rotation=90, va='bottom', ha = 'right')
    
    plt.tight_layout()
    plt.show()
    



def plotsingle(d):
    d.index = list(range(len(d)))
    ax = d.plot()
    for j,s in enumerate(chapters):
            ax.text(j, 0, '     '+s , size = 'xx-small', rotation=90, va='top', ha = 'left')

    ax.get_xaxis().set_ticks([])
    plt.tight_layout()
    plt.show()


def legend(df):
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D


    legend_elements = [Patch(facecolor=COLORS[i], edgecolor='whitesmoke', label=k) for i,k in enumerate(df.columns)]

    # Create the figure
    fig, ax = plt.subplots()
    ax.legend(handles=legend_elements, loc='center')

    plt.show()