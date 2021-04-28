# analysis_plots.py
# Plot output functions for analysis of Fisher's iris data set
# Author: Fiachra O' Donoghue

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


"""
These functions abstract away some of the details of producing 
plots from the iris dataset while also providing a simple interface
for some basic tinkering with the plots. 

Keeping these functions in a dedicated plots file will hopefully keep
the main analysis file more manageable in terms of length and comlexity.
"""

def label_grid(grid, axis_labels=None, title=None):
# Helper function for labeling axes and titling Seaborn facetgrids

    # Set subplot titles
    grid.set_titles(col_template="{col_name}", row_template="{row_name}")

    # Set axis labels if provided
    if axis_labels:
        grid.set_axis_labels(axis_labels)

    # Set grid title if provided    
    if title:
        grid.fig.subplots_adjust(top=0.85)
        grid.fig.suptitle(title)


def histograms(data=None, filename=None, title=None):
# generate stacked histograms from the passed long-form dataframe

    # Select a clean minimal Seaborn theme
    sns.set_theme(style="white")

    # displot is a seaborn function for generating multiple faceted distribution plots
    h = sns.displot(data=data, 
                x="value", 
                multiple="stack",
                hue="class",
                col="variable", 
                kind="hist", 
                kde=False, 
                common_bins=True, 
                col_wrap=2,
                facet_kws=dict(sharex=False, 
                               sharey=True,
                               margin_titles=True)
            )

    # Generate grid title and labels
    label_grid(h, axis_labels="value (cm)", 
                  title=title)

    # Save to specified path
    if filename:
        h.savefig(filename)


def catplots(data=None, filename=None, title=None):
    h = sns.catplot(data=data, 
                x="value", 
                y="class", 
                col="variable", 
                kind="box", 
                sharex=False)

    # Generate grid title and labels
    label_grid(h, axis_labels="value (cm)", 
                  title=title)

    # Save to specified path
    if filename:
        h.savefig(filename)


def stripplot(data=None, title=None, filename=None):
# Stripplot

    plt.clf()
    sns.set_style("white")
    h = sns.stripplot(data=data, 
                      y="value", 
                      x="variable", 
                      hue="class", 
                      jitter=0.2, 
                      dodge=False)
    
    # Set title if specified
    if title:                  
        h.set(title=title)

    # Save to specified path
    if filename:
        plt.savefig(filename)


def scatterplot(data=None, x=None, y=None, overlay_data=None, 
                title=None, filename=None):

    

    

    # Set title if specified
    if title:                  
        h.set(title=title)

    # Save to specified path
    if filename:
        plt.tight_layout()
        plt.savefig(filename)



def ecdfs():
    pass



def pairplots():
    pass

