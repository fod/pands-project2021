# analysis.py
# Perform various analyses on Fisher's Iris dataset
# Author: Fiachra O' Donoghue

# Imports
import pandas as pd
import numpy as np
#import matplotlib.pyplot as pyplot
#import seaborn as sns

# Read iris data from csv file
iris = pd.read_csv("iris_data/bezdekIris.data", 
names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "class"])

# Iris data now in iris pandas dataframe
# Generate decriptive statistics for entire dataset
full_summary = iris.describe().round(decimals=2)

# write summary stats to file
full_summary.to_html("summary_stats.html")
#np.savetxt("summary_stats.txt", full_summary, fmt="%.2f") # https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html

with open("summary_stats.md", "w+") as f:
    f.write(full_summary.to_markdown())     # To read this back: https://stackoverflow.com/questions/60154404/is-there-the-equivalent-of-to-markdown-to-read-data

# Descriptive stats for each iris species
class_summaries = iris.groupby(iris["class"]).describe().round(decimals=2).transpose()
print(class_summaries)

#Histogram, bee swarm, violin, box, ECDF, scatter
#Correlation, covariance, ρ (Pearson correlation): covariance/(std(x))(std(y)) =
# variability due to codependence / independent variability

#Probability of misclassification