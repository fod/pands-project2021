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


def histograms(data=None, filename="", mean_lines=True, title=None):

    # Set plot style
    sns.set()

    # Generate plot. Although this draws a grid of related plots
    # in this case the histograms do not share bins or scales
    # As such they should be each considered in isolation. This 
    # is just a convenient method to view the broad structure of
    # each feature/class combination 
    g = sns.displot(
                data=data,              
                x="value", 
                row="class",
                hue="class",
                col="variable", 
                kind="hist", 
                kde=False, 
                common_bins=False,
                height=3.5, 
                aspect=1, 
                alpha=1, 
                linewidth=1,
                facet_kws=dict(
                    sharex=False, 
                    sharey=False,
                    margin_titles=True
                )
            )

    # Mean lines
    def vml(x, **kwargs):
        plt.axvline(np.mean(x), linestyle = '--', color = 'yellow', linewidth=2, label="mean=" + str(np.mean(x)))
   
    # Draw mean lines if requested
    if mean_lines:
        g.map(vml, "value")

    # Add grid title if one has been specified
    if title:
        g.fig.subplots_adjust(top=0.9)
        g.fig.suptitle(title)

    # x-axis labels
    g.set_axis_labels("value (cm)")

    # Column titles
    g.set_titles(col_template="{col_name}", row_template="{row_name}")

    # Remove extraneous axis lines
    g.despine(left=True)

    # Save image file
    g.savefig(filename)



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