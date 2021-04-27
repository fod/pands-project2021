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

    label_grid(h, axis_labels="value (cm)", 
                  title="Stacked Feature Histograms for each Iris Species")

    # Save to specified path
    if filename:
        h.savefig(filename)


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


def ecdfs():
    pass

def stripplots():
    pass

def catplots(data=None, filename=None, title=None):
    h = sns.catplot(data=data, 
                x="value", 
                y="class", 
                col="variable", 
                kind="box", 
                sharex=False)

    # Add title if one has been specified
    if title:
        h.fig.suptitle(title)
    
    # Save to specified path
    if filename:
        h.savefig(filename)


def pairplots():
    pass

def jointplots():
    pass