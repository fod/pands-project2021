# utility_functions.py
# Useful functions for analysing Fisher's Iris Dataset
# Author: Fiachra O' Donoghue

import pandas as pd

def full_description(df, filename, output_style=None):

    # Generate full statistical summary of the dataset as pandas dataframe, 
    # rounding all numbers to 2 decimal places
    full_summary = df.describe.round(decimals=2)

    # Create a file if necessary and open it for writing 
    # then write the summary to a table suitable for display in a Github readme
    with open(filename, "w+") as f:
    #ref re tblformat: https://pypi.org/project/tabulate/
    # To read this back: https://stackoverflow.com/questions/60154404/is-there-the-equivalent-of-to-markdown-to-read-data
        f.write(full_summary.to_markdown(tablefmt="github"))


