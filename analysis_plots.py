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

def histograms_stacked(data=None, filename=""):
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
            common_bins=True, 
            col_wrap=2,
            facet_kws=dict(sharex=False, 
                           sharey=False,
                           margin_titles=True)
           )

    h.set_axis_labels("value (cm)")
    h.set_titles(col_template="{col_name}", row_template="{row_name}")

    # Add grid title if one has been specified
    if title:
        g.fig.subplots_adjust(top=0.8)
        g.fig.suptitle(title)

    h.fig.subplots_adjust(top=0.8)
    h.fig.suptitle("Stacked Feature Histograms for each Iris Species")
    h.savefig(filename)

def histograms(data=None, filename=None, title=None):    
    sns.set_theme(style="white")
    h = sns.displot(data=data, 
                x="value", 
                #row="class",
                multiple="stack",
                hue="class",
                col="variable", 
                kind="hist", 
                kde=False, 
                common_bins=True, 
                facet_kws=dict(sharex=False, 
                            sharey=True,
                            margin_titles=True)
            )

    h.set_axis_labels("value (cm)")
    h.set_titles(col_template="{col_name}", row_template="{row_name}")

    if title:
        h.fig.subplots_adjust(top=0.85)
        h.fig.suptitle(title)
    
    if filename:
        h.savefig(filename)


def ecdfs():
    pass

def stripplots():
    pass

def catplots():
    pass

def pairplots():
    pass

def jointplots():
    pass