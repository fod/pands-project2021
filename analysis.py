# analysis.py
# Perform various analyses on Fisher's Iris dataset
# Author: Fiachra O' Donoghue

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns

# Read iris data from csv file
iris = pd.read_csv("iris_data/bezdekIris.data", 
names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "class"])

