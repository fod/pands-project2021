# The Fisher Iris Data Set

HDip Data Analytics Programming and Scripting Project

## Introduction
Fisher's Iris Data set is a collection of 50 observations of four measurements — sepal length, sepal width, petal length, and petal width from each of three plant species: *Iris setosa*, *I. versicolor*, and *I. virginica*. Two of these sets (*I. setosa* and *I. versicolor*) were collected from plants growing together in the same colony, while the third (*I. virginica*) was collected from elsewhere (Fisher, 1936). *I. setosa* is linearly separable from the other two species based on a function of the four measurements recorded whereas *I. vesicolor* and *I. virginica* are not (*ibid.*).

## Significance


The dataset used for this project was downloaded from the UCI Machine Learning Repository (Dua and Graff, 2019)


## Tasks
### EDA
1. Generate descriptive statistics for the dataset.
    [link](summary_stats.csv)

    <table border="1" class="dataframe" style="font-size: 0.7em">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal Length</th>
      <th>Sepal Width</th>
      <th>Petal Length</th>
      <th>Petal Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>150.00</td>
      <td>150.00</td>
      <td>150.00</td>
      <td>150.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.84</td>
      <td>3.06</td>
      <td>3.76</td>
      <td>1.20</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.83</td>
      <td>0.44</td>
      <td>1.77</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.30</td>
      <td>2.00</td>
      <td>1.00</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.10</td>
      <td>2.80</td>
      <td>1.60</td>
      <td>0.30</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.80</td>
      <td>3.00</td>
      <td>4.35</td>
      <td>1.30</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.40</td>
      <td>3.30</td>
      <td>5.10</td>
      <td>1.80</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.90</td>
      <td>4.40</td>
      <td>6.90</td>
      <td>2.50</td>
    </tr>
  </tbody>
</table>


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