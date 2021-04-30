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

def label_grid(grid, axis_labels=None, title=None, grid_titles=False):
# Helper function for labeling axes and titling Seaborn facetgrids

    # Set subplot titles
    if grid_titles:
        grid.set_titles(col_template="{col_name}", row_template="{row_name}")

    # Set axis labels if provided
    if axis_labels:
        grid.set_axis_labels(axis_labels)

    # Set grid title if provided    
    if title:
        grid.fig.subplots_adjust(top=0.9)
        grid.fig.suptitle(title)


def histograms(data=None, filename=None, title=None):
# Generate stacked histograms from the passed long-form dataframe

    # Select a clean minimal Seaborn theme
    sns.set_theme(style="white")

    # displot is a seaborn function for generating multiple faceted distribution plots
    # See: https://seaborn.pydata.org/generated/seaborn.displot.html
    g = sns.displot(data=data, 
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
    label_grid(g, axis_labels="value (cm)", 
                  title=title, grid_titles=True)

    # Save to specified path
    if filename:
        g.savefig(filename)


def boxplots(data=None, filename=None, title=None):
# Generate faceted boxplots based on the passed long-form dataframe

    # catplot is a seaborn function for generating multiple faceted categorical plots
    # See: https://seaborn.pydata.org/generated/seaborn.catplot.html
    g = sns.catplot(data=data, 
                    x="value", 
                    y="class", 
                    col="variable", 
                    kind="box", 
                    sharex=False)

    # Generate grid title and labels
    label_grid(g, axis_labels="value (cm)", 
                  title=title, grid_titles=True)

    # Save to specified path
    if filename:
        g.savefig(filename)


def stripplot(data=None, title=None, filename=None):
# Generate a stripplot from the passed long-form dataframe

    # Clear the current  matplotlib figure
    plt.clf()

    # Select a clean Seaborn theme with gridlines
    sns.set_style("whitegrid")

    # Generate the stripplot
    # See http://seaborn.pydata.org/generated/seaborn.stripplot.html
    g = sns.stripplot(data=data, 
                      y="value", 
                      x="variable", 
                      hue="class", 
                      jitter=0.2, 
                      dodge=False)
    
    # Set title if specified
    if title:                  
        g.set(title=title)

    # Save to specified path
    if filename:
        plt.savefig(filename)


def scatterplot(data=None, x=None, y=None, overlay=None, 
                title=None, filename=None):
# Generate a jointplot (relational plot with edge distribution plots)
# from passed wide-form dataframe with an optional second dataframe overlaid

    # Clear the current  matplotlib figure
    plt.clf()

    # Generate the jointplot
    # See http://seaborn.pydata.org/generated/seaborn.jointplot.html
    g = sns.jointplot(data=data, 
                      x=x, 
                      y=y, 
                      hue="class", 
                      kind="scatter",
                      s=15,
                      # Preserve colours used in other plots for versicolor and virginica
                      palette=[sns.color_palette()[1],sns.color_palette()[2]]) 

    # Overlay the second dataset
    # Specifically in this case draw red circles around passed points
    if overlay:
        g.ax_joint.scatter(overlay["x"], 
                           overlay["y"], 
                           facecolors='none', 
                           edgecolors='red', 
                           s=30, 
                           label=overlay["label"], 
                           alpha=0.5)

        # Add the overlaid data to the legend
        g.ax_joint.legend()

    # Set title if specified
    if title:                  
        g.fig.suptitle(title)

    # Save to specified path
    if filename:
        plt.tight_layout()
        plt.savefig(filename)


def ecdfs(data=None, x=None, col=None, title=None, filename=None, vlines=False, span=False):
# Generate faceted ecdf plots from passed long-form dataframe

    # Clear the current  matplotlib figure
    plt.clf()

    # Select a clean Seaborn theme with gridlines
    sns.set_style("whitegrid")

    # displot is a seaborn function for generating multiple faceted distribution plots
    # See: https://seaborn.pydata.org/generated/seaborn.displot.html
    g = sns.displot(data=data, 
                    x=x, 
                    col=col, 
                    hue="class", 
                    kind="ecdf", 
                    linewidth=2, 
                    facet_kws=dict(sharex=False),
                    col_wrap=2)
    
    def vertical_line(x, **kwargs):
    # Nested function for drawing vertical lines at max values of passed series

        for n in (x[:50], x[50:100], x[100:]):
            plt.axvline(np.max(n), linestyle = '--', color = 'red', linewidth=1, label="Max")
            # plt.axvline(np.min(n), linestyle = '--', color = 'pink', linewidth=2, label="Min")

    if vlines:
        # Draw the max lines in ECDF facets
        g.map(vertical_line, "value")

    def span(x, **kwargs):
        # Nested function for highlighting min virginica and max versicolor
        max_vers = np.max(x[50:100])
        min_virg = np.min(x[100:])
        plt.axvspan(max_vers, min_virg, color="red", alpha=0.2)

    if span:
        # Draw the overlap spans in ECDF facets
        g.map(span, "value")

    # Label y-axes
    g.set_ylabels("proportion")

    # Generate grid title and labels
    label_grid(g, "value (cm)", title, grid_titles=True)  

    # Save to specified path
    if filename:
        plt.savefig(filename)


def pairplots(data=None, title=None, filename=None):
# Generate faceted scatterplots for all 
# feature pairs of passed long-form dataset
    
    # pairplot is a Seaborn function for generating grids of relational plots
    g = sns.pairplot(data, hue="class", kind="scatter")

    # Generate grid title
    label_grid(g, title=title)

    # Save to specified path
    if filename:
        plt.savefig(filename)


