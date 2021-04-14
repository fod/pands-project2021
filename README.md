# The Fisher Iris Data Set

HDip Data Analytics Programming and Scripting Project

## Introduction
Fisher's Iris Data set is a collection of 50 observations of four measurements — sepal length, sepal width, petal length, and petal width from each of three plant species: *Iris setosa*, *I. versicolor*, and *I. virginica*. Two of these sets (*I. setosa* and *I. versicolor*) were collected from plants growing together in the same colony, while the third (*I. virginica*) was collected from elsewhere (Fisher, 1936). *I. setosa* is linearly separable from the other two species based on a function of the four measurements recorded whereas *I. vesicolor* and *I. virginica* are not (*ibid.*).

## Significance


The dataset used for this project was downloaded from the UCI Machine Learning Repository (Dua and Graff, 2019)


## Tasks
### EDA
1. Generate descriptive statistics for the dataset.
    [link](summary_stats.md)



|       |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width |
|-------|----------------|---------------|----------------|---------------|
| count |         150    |        150    |         150    |        150    |
| mean  |           5.84 |          3.06 |           3.76 |          1.2  |
| std   |           0.83 |          0.44 |           1.77 |          0.76 |
| min   |           4.3  |          2    |           1    |          0.1  |
| 25%   |           5.1  |          2.8  |           1.6  |          0.3  |
| 50%   |           5.8  |          3    |           4.35 |          1.3  |
| 75%   |           6.4  |          3.3  |           5.1  |          1.8  |
| max   |           7.9  |          4.4  |           6.9  |          2.5  |



2. Generate histograms for each measurement
3. Generate scatterplots / pairplots for all of the variables
4. Examine some other descriptive plots:
    1. Box plot
    2. Violin plot
    3. Bee swarm plot
    4. Empirical Cumulative Distribution Function (eCDF)

### Correlation
1. Covariance
2. ρ (Pearson correlation)
3. Variability due to codependence / independent variability

### Separation improvement
1. Dimensionality reduction
    1. LDA
    2. PCA

### Uncertainty measurement
1. Probability of misclassification
2. identification of high probability areas
3. Identification on plots of areas with higher likelihood of misclassification (density surface?)

### Machine learning
1. Unsupervised classification
2. Supervised classification
3. Function estimation

## References

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. 

Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems, Annual Eugenics, 7, Part II, 179-188 