# analysis.py
# Perform various analyses on Fisher's Iris dataset
# Author: Fiachra O' Donoghue

# Imports
import pandas as pd
import numpy as np
import fileinput
from analysis_util import *

#import matplotlib.pyplot as pyplot
#import seaborn as sns





def summarise(iris):
# Summarise the dataframe; returns two datframes, one with descriptive statistics
# relating to the entire dataset, and one grouped by iris variety
 
    # Generate full statistical summary of the dataset as pandas dataframe, 
    # rounding all numbers to 2 decimal places
    full_summary = iris.describe().round(decimals=2)

    # Descriptive statistics per class, multilevel index consisting of measurement and statistic
    class_summaries = iris.groupby(iris["class"]).describe().round(decimals=2).transpose()

    return (full_summary, class_summaries)



def markdown_table(class_summaries):
# Write class summaries to four markdown tables, one
# for each measurement and each with a column for class

    # Tidy up the dataframe for a human readable table
    summaries_table = class_summaries.reset_index().rename(columns={"level_1":""})

    # Get unique values for class (iris variety names)
    for m in set(summaries_table["level_0"]):

        # Drop the measurement column as it just repeats the same value for each table
        sub_table = summaries_table[summaries_table["level_0"] == m].drop("level_0", axis=1)
        # Measurement name (table title)
        table = f"{m}:\n{sub_table.to_markdown(index=False, tablefmt="github")}\n\n"

        print(table)





# d = {"TABLE1": full_summary.to_markdown(tablefmt="github")}
# insert_text("README.md", d)





# try:
#     # Write class summaries to four markdown tables, one for each measurement and each with
#     # a column for class
#     with open("output/class_summaries.md", "w+") as md, open("output/class_summaries.csv", "w+") as csv:

#         # Get unique values for class (iris variety names)
#         for m in set(summaries_table["level_0"]):

#             # Drop the measurement column as it just repeats the same value for each table
#             sub_table = summaries_table[summaries_table["level_0"] == m].drop("level_0", axis=1)
#             # Measurement name (table title)
#             md.write(f"{m}:\n")

#             # Write markdown table for humans
#             md.write(sub_table.to_markdown(index=False, tablefmt="github"))
#             md.write("\n\n")

#             # Write csv table for other applications
#             csv.write(summaries_table.to_csv())

# except IOError as e:
#     print(f"File error: {e}")



def main():
    colnames = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "class"]
    iris_path = "iris_data/bezdekIris.data"
    iris = csv_to_df(iris_path, colnames)


# Histogram, bee swarm, violin, box, ECDF, scatter
# Correlation, covariance, ρ (Pearson correlation): covariance/(std(x))(std(y)) =
# variability due to codependence / independent variability

# Probability of misclassification


if __name__ == "__main__":
    main()