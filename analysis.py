# analysis.py
# Perform various analyses on Fisher's Iris dataset
# Author: Fiachra O' Donoghue

# Imports
import pandas as pd
import numpy as np
import fileinput
from analysis_util import insert_text, csv_to_df, df_to_csv

#import matplotlib.pyplot as pyplot
#import seaborn as sns


def summarise(iris):
# Summarise the dataframe; returns two dataframes, one with descriptive statistics
# relating to the entire dataset, and one grouped by iris variety
 
    # Generate full statistical summary of the dataset as pandas dataframe, 
    # rounding all numbers to 2 decimal places
    full_summary = iris.describe().round(decimals=2)

    # Descriptive statistics per class, multilevel index consisting of feature and statistic
    class_summaries = iris.groupby(iris["class"]).describe().round(decimals=2).transpose()

    return (full_summary, class_summaries)



def output_table(class_summaries):
# Write class summaries to four markdown tables, one
# for each feature and each with a column for class

    # Tidy up the dataframe for a human readable table by:
    # 1) remove multilevel index (feature type and statistic)
    # 2) remove automatic column name from "statistic" column
    summaries_table = class_summaries.reset_index().rename(columns={"level_1":""})

    # Declare dict to hold the generated markdown tables
    tables = {}

    # Get unique values for class (iris variety names)
    for m in set(summaries_table["level_0"]):

        # Drop the feature column as it just repeats the same value for each table
        sub_table = summaries_table[summaries_table["level_0"] == m].drop("level_0", axis=1)

        # Generate table in Github-style markdown and add some newlines for spacing
        md_table = sub_table.to_markdown(index=False, tablefmt="github")
        table = md_table + "\n\n"

        # Add the table to the tables dict with the feature name as key
        tables[m] = table

    return tables


def main():

    # Column names and file path for iris dataset
    colnames = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "class"]
    iris_path = "iris_data/bezdekIris.data"

    # Load csv data to pandas dataframe
    iris = csv_to_df(iris_path, colnames)

    # Create data frames containing full summary (descriptive statistics across entire dataset) 
    # and class summaries (descriptive statistics grouped by iris variety) 
    full_summary, class_summaries = summarise(iris)

    # Generate a dict of tables in github markdown format. 
    # The keys will be used to insert them into README.md
    tables = output_table(class_summaries)

    #Add the entire dataset statistics table to the dict of markdown tables
    tables["Full Summary"] = full_summary.to_markdown(tablefmt="github")

    # Insert the tables at the appropriate locations in README.md
    insert_text("README.md", tables)

    # Save descriptive stats to csv files
    df_to_csv("output/full.csv", full_summary)
    df_to_csv("output/class.csv", class_summaries)

# Histogram, bee swarm, violin, box, ECDF, scatter
# Correlation, covariance, ρ (Pearson correlation): covariance/(std(x))(std(y)) =
# variability due to codependence / independent variability

# Probability of misclassification


if __name__ == "__main__":
    main()






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