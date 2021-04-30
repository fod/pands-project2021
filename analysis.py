# analysis.py
# Perform various analyses on Fisher's Iris dataset
# Author: Fiachra O' Donoghue

# Imports
import pandas as pd
import numpy as np

# analysis_util provides a templating system to populate README.md 
# and some data conversion functions
from analysis_util import insert_text, csv_to_df, df_to_csv

# analysis_plots provides all of the plotting code for this project
from analysis_plots import histograms, boxplots, stripplot, scatterplot, ecdfs, pairplots


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

    # Generate head() and insert into README
    insert_text("README.md", {"Iris Head": iris.head().to_markdown(tablefmt="github")})

    # Generate counts by class and insert into README
    insert_text("README.md", {"Counts": iris.groupby("class").count().to_markdown(tablefmt="github")})

    # Generate long-form iris dataset
    iris_long = iris.melt(value_vars=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"], id_vars="class")

    # Generate head() and insert into README
    insert_text("README.md", {"Long-form Head": iris_long.head().to_markdown(tablefmt="github")})

    # Generate histograms and insert into README
    histograms(data=iris_long, 
               filename="output/histograms_stacked.png", 
               title="Stacked Feature Histograms for each Iris Species")
    insert_text("README.md", 
               {"Stacked Histograms": "![Stacked Histograms](" + "output/histograms_stacked.png" + ")"})
  
    # Generate boxplots and insert into README
    boxplots(data=iris_long, 
             filename="output/boxplots.png", 
             title="Comparison of Features per Class Using Boxplots")
    insert_text("README.md", 
                {"Boxplots": "![Boxplots](" + "output/boxplots.png" + ")"})

    # Generate stripplot and insert into README
    stripplot(data=iris_long, 
             filename="output/stripplot.png", 
             title="Stripplot demonstrating distribution and degree of separation of each class by feature")
    insert_text("README.md", 
                {"Stripplot": "![Stripplot](" + "output/stripplot.png" + ")"})

    # Generate ECDF Plots and insert into README
    ecdfs(data=iris_long,
          x="value",
          col="variable",
          vlines=True,
          title="Empirical Cumulative Distribution Function (ECDF) with maximum values indicated",
          filename="output/ecdf.png")
    insert_text("README.md", 
                {"ECDF": "![ECDF](" + "output/ecdf.png" + ")"})

    # Generate Petal Width == 1.8 table for ecdf discussion
    # and insert into README
    max_petal_width = np.max(iris[iris["class"]=="Iris-versicolor"]["Petal Width"])
    max_petal_width_tbl = iris[iris["Petal Width"]==max_petal_width]
    insert_text("README.md", 
                {"Petal Width = 1.8": max_petal_width_tbl.to_markdown(tablefmt="github")})


    # Generate pairplots and insert into README
    pairplots(data=iris, 
              title="Scatter plots of all feature combinations in iris dataset",
              filename="output/pairplot.png")
    insert_text("README.md", 
                {"Pairplot": "![Pairplot](" + "output/pairplot.png" + ")"})

    # Add area columns to iris dataframe
    iris["Sepal Area"] = iris["Sepal Length"] * iris["Sepal Width"]
    iris["Petal Area"] = iris["Petal Length"] * iris["Petal Width"]

    # Generate difficult to classify subset of Iris dataset
    iris_rule = iris[(iris["Petal Length"] >= 4.5) & 
                     (iris["Petal Length"] <= 5.1) & 
                     (iris["Petal Width"] >= 1.4) & 
                     (iris["Petal Width"] <= 1.8)]

    # Remove easily classified I. setosa from dataframe
    iris_sub = iris[iris["class"].isin(["Iris-virginica", "Iris-versicolor"])]


    # Calculate correlation matrix and insert into README
    insert_text("README.md", 
                {"Correlation": iris.corr().to_markdown(tablefmt="github")})

    # Generate ECDF Plots and insert into README
    ecdfs(data=iris_long[iris_long["variable"].isin(["Petal Length", "Petal Width"])],
          x="value",
          col="variable",
          vspan=True,
          title="Empirical Cumulative Distribution Function (ECDF) with overlaps highlighted",
          filename="output/ecdf_spans.png")
    insert_text("README.md", 
                {"ECDF SPANS": "![ECDF SPANS](" + "output/ecdf_spans.png" + ")"})

    # Generate Petal scatterplot and insert into README
    scatterplot(data=iris_sub, 
                x="Petal Length", 
                y="Petal Width", 
                overlay={"x": iris_rule["Petal Length"],
                         "y": iris_rule["Petal Width"],
                         "label": "Difficult to classify"},
                title="Petal Length x Petal Width with Difficult-to-Classify\nObservations Highlighted",
                filename="output/scatter_petal.png")
    insert_text("README.md", 
                {"Classification Petal": '<img src="' + 'output/scatter_petal.png"' + ' height=500>'})

    # Generate Sepal scatterplot and insert into README
    scatterplot(data=iris_sub, 
                x="Sepal Length", 
                y="Sepal Width", 
                overlay={"x": iris_rule["Sepal Length"],
                         "y": iris_rule["Sepal Width"],
                         "label": "Difficult to classify"},
                title="Sepal Length x Sepal Width with Difficult-to-Classify\nObservations Highlighted",
                filename="output/scatter_sepal.png")
    insert_text("README.md", 
                {"Classification Sepal": '<img src="' + 'output/scatter_sepal.png"' + ' height=500>'})

    # Plot areas and insert into README
    scatterplot(data=iris_sub, 
                x="Petal Area", 
                y="Sepal Area", 
                overlay={"x": iris_rule["Petal Area"],
                         "y": iris_rule["Sepal Area"],
                         "label": "Difficult to classify"},
                title="Petal Area x Sepal Area with Difficult-to-Classify\nObservations Highlighted",
                filename="output/scatter_area.png")
    insert_text("README.md", 
                {"Classification Area": '<img src="' + 'output/scatter_area.png"' + ' height=500>'})





if __name__ == "__main__":
    main()

