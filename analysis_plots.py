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


def histograms(data):
    sns.set()
    g = sns.displot(data=data, 
                x="value", 
                row="class",
                hue="class",
                col="variable", 
                kind="hist", 
                kde=False, 
                common_bins=False,
                #    bins=40,
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

    def vml(x, **kwargs):
        plt.axvline(np.mean(x), linestyle = '--', color = 'yellow', linewidth=2, label="mean=" + str(np.mean(x)))

    g.map(vml, "value")
    g.set_axis_labels("value (cm)")
    g.set_titles(col_template="{col_name}", row_template="{row_name}")
    g.despine(left=True)
    g.savefig("hist_delme.png")

def ecdfs():
    pass

def stripplots():
    pass

def catplots():
    pass