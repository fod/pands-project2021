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

   

# # Descriptive stats for each iris species
# class_summaries = iris.groupby(iris["class"]).describe().round(decimals=2).transpose().reset_index()

# with open("class_summaries.md", "w+") as f:
#     f.write(class_summaries.to_markdown(index=False))

# Descriptive statistics per class
class_summaries = iris.groupby(iris["class"]).describe().round(decimals=2).transpose()
class_summaries = class_summaries.reset_index().rename(columns={"level_1":""})

with open("class_summaries.md", "w+") as f:
    for m in set(class_summaries["level_0"]):
        f.write(f"{m}:\n")
        cc = class_summaries[class_summaries["level_0"] == m].drop("level_0", axis=1)
        f.write(cc.to_markdown(index=False, tablefmt="github"))
        f.write("\n\n")

#Histogram, bee swarm, violin, box, ECDF, scatter
#Correlation, covariance, ρ (Pearson correlation): covariance/(std(x))(std(y)) =
# variability due to codependence / independent variability

#Probability of misclassification