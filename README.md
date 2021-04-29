# The Fisher Iris Data Set

HDip Data Analytics Programming and Scripting Project

<!-- TOC -->

- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to run this project](#how-to-run-this-project)
- [Data preparation](#data-preparation)
- [Descriptive Statistics](#descriptive-statistics)
    - [Visualisation of Descriptive Statistics](#visualisation-of-descriptive-statistics)
        - [Histograms](#histograms)
        - [Boxplots](#boxplots)
        - [Stripplots](#stripplots)
        - [ECDF Empirical Cumulative Distribution Function](#ecdf-empirical-cumulative-distribution-function)
- [Relationships](#relationships)
    - [Correlation](#correlation)
    - [Visualisation of Relationships](#visualisation-of-relationships)
    - [Separation improvement](#separation-improvement)
- [Further Study](#further-study)
    - [Uncertainty measurement](#uncertainty-measurement)
    - [Machine learning](#machine-learning)
- [References](#references)

<!-- /TOC -->

## Introduction
Fisher's Iris Data set is a collection of 50 observations of four measurements — sepal length, sepal width, petal length, and petal width from each of three plant species: *Iris setosa*, *I. versicolor*, and *I. virginica*. Two of these sets (*I. setosa* and *I. versicolor*) were collected from plants growing together in the same colony, while the third (*I. virginica*) was collected from a separate site (Fisher, 1936). *I. setosa* is linearly separable from the other two species based on some of the four measurements recorded whereas *I. vesicolor* and *I. virginica* are not (*ibid.*).

This project uses the Python programming language to perform an exploratory data analysis (EDA) on the iris dataset and to examine some approaches to data classification using Python libraries.

## Requirements

This project was made using the following Python version and package versions:

- [Python 3.9.3](https://www.python.org/downloads/release/python-393/)
- [pandas 1.2.4](https://pandas.pydata.org/docs/)
- [numpy 1.19.2](https://numpy.org/)
- [matplotlib 3.3.4](https://matplotlib.org/)
- [seaborn 0.11.1](https://seaborn.pydata.org/)

## How to run this project

The code in this project is spread over three files:

1. [```analysis.py```](analysis.py). This file contains the main project code. It consists of three functions:  
   
   i. ```summarise()```, which produces descriptive statistics for the dataset as a whole and for the dataset broken down by class (iris variety),

   ii. ```output_table()```, which produces a dict of GitHub Markdown formatted tables containing the descriptive statistics produced by ```summarise()``` above, and
   
   iii. ```main()```, which consists of a series of commands — primarily calling on functions defined in [```analysis_util.py```](analysis_util.py) and [```analysis_plots.py```](analysis_plots.py) — to manipulate the data, generate plots, and write the result to this README file.

2. [```analysis_util.py```](analysis_util.py). This file contains code which helps generate the structure of the project and in particular this README file. It consists of three functions, two of which (```csv_to_df()``` and ```df_to_csv()```) are thin wrappers around the [```pandas```](https://pandas.pydata.org/) functions ```pandas.read_csv()``` [REF] and ```DataFrame.to_csv()``` [REF]. The third function is ```insert_text()```, which, passed a dictionary consisting of labels and a file path, searches the target file for the keys of the passed dictionary in the form ```{% KEY %}``` and inserts, at that position, whatever content that key holds as its value. This function is used to insert all of the tables and plots generated by [```analysis.py```](analysis.py) at the correct positions in this README file.

3. [```analysis_plots.py```](analysis_plots.py). This file contains all of the code for generating the plots used in this project. Most of the functions are thin wrappers around plotting functions from the [```Seaborn```](https://seaborn.pydata.org/) plotting library with many of the parameters preselected. This functionality is given its own file in order to reduce the length and complexity of the main analysis file. The file contains seven functions, one of which, ```label_grid()```, is a helper function to help avoid code duplication in the application of labels to certain types of faceted plots, and the rest — ```histograms()```, ```boxplots()```, ```stripplot()```, ```scatterplot```, ```ecdfs()```, and ```pairplots()``` — are used to generate the various plots examined in this project.

The [```output```](output/) directory contains descriptive statistics in csv format, and all of the plots used in this report, in png format. The [```iris_data```](iris_data/) directory contains all of the files pertaining to Fisher's iris data which were downloaded for the project. If the [```analysis.py```](analysis.py) file is run, and the correct libraries are available, the [```output```](output/) directory is populated with CSV files and images, and this current (README) file is populated with tables and links to the images that are output during the program run.


## Data preparation

The dataset used for this project was downloaded from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris/) (Dua and Graff, 2019).
The data as downloaded consists of three files: [iris.data](iris_data/iris.data); the dataset as originally uploaded to the repository, [bezdekIris.data](iris_data/bezdekIris.data); the same data with some errors corrected (ibid.), and [iris.names](iris_data/iris.names); a description of the data along with some summary statistics noting, in particular, a high correlation between class and both petal length and petal width.

The data is imported to a pandas ```DataFrame``` (hereafter referred to informally as dataframe) using ```pandas.read_csv()``` (REF). The output of a call to ```DataFrame.head()``` which returns the top five rows of a dataframe (REF) is reproduced below:

<!-- {% Iris Head %} -->

|    |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width | class       |
|----|----------------|---------------|----------------|---------------|-------------|
|  0 |            5.1 |           3.5 |            1.4 |           0.2 | Iris-setosa |
|  1 |            4.9 |           3   |            1.4 |           0.2 | Iris-setosa |
|  2 |            4.7 |           3.2 |            1.3 |           0.2 | Iris-setosa |
|  3 |            4.6 |           3.1 |            1.5 |           0.2 | Iris-setosa |
|  4 |            5   |           3.6 |            1.4 |           0.2 | Iris-setosa |

<!-- {% END %} -->

The data has been organised such that the values for each of the four features — Sepal Length, Sepal Width, Petal Length, and Petal Width — are held in their own columns, while a fifth column designates the class, or species. Calling ```iris["class"].unique()``` returns ```array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)```, demonstrating that the class column contains 3 unique values; Iris-setosa, Iris-versiolor, and Iris-virginica. Each row of the dataframe represents a separate observation.

Grouping the dataset by class shows there are 50 observations of each of the 4 variables for each class:

```iris.groupby("class").count()```

<!-- {% Counts %} -->

| class           |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width |
|-----------------|----------------|---------------|----------------|---------------|
| Iris-setosa     |             50 |            50 |             50 |            50 |
| Iris-versicolor |             50 |            50 |             50 |            50 |
| Iris-virginica  |             50 |            50 |             50 |            50 |

<!-- {% END %} -->

The dataframe as described holds the data in 'wide' format, i.e. observations are in rows and variables are in columns, each row holding observations for a number of variables ([REF](https://seaborn.pydata.org/tutorial/data_structure.html)). This is a useful format for some applications, and it is certainly a good compact and intuitive format for visual examination; however, it will also be necessary to generate a 'long' format dataframe, in which each row contains just a single observation. This format is often more flexible for plotting as columns can simply be assigned to, for instance, x-axis, y-axis, colour, etc. There are cases where one is more convenient than the other and both are used here.

The pandas ```DataFrame.melt()``` method transforms a wide-form dataframe to a long form one by placing all of the values in one column and adding columns for the grouping variables ([REF](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.melt.html)). The output of ```DataFrame.head()``` on the long-form dataframe is shown below:

<!-- {% Long-form Head %} -->

|    | class       | variable     |   value |
|----|-------------|--------------|---------|
|  0 | Iris-setosa | Sepal Length |     5.1 |
|  1 | Iris-setosa | Sepal Length |     4.9 |
|  2 | Iris-setosa | Sepal Length |     4.7 |
|  3 | Iris-setosa | Sepal Length |     4.6 |
|  4 | Iris-setosa | Sepal Length |     5   |

<!-- {% END %} -->

<hr>

## Descriptive Statistics

Descriptive statistics for the dataset can be generated using the pandas ```DataFrame.describe()``` method. The count, mean, standard deviation, minimum value, maximum value, the median, and the first and third quartiles for each feature are calculated for the dataset as a whole. The result is shown in the table below. The data in this table has also been output to [```output/full.csv```](output/full.csv) in CSV format using the ```DataFrame.to_csv()``` method.

<!-- {% Full Summary %} -->

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

<!-- {% END %} -->

Some useful information can be gleaned from this table even before the data is broken down by class for a finer-grained examination. Some observations that can be made are:

1. Sepals, with mean dimensions of 5.84 cm × 3.06 cm tend to be considerably larger than petals (3.76 × 1.2).
2. Petal size, on the other hand is much more variable than sepal size, as indicated both by the petal length standard deviation (1.77), and the range of petal lengths(6.9 - 1 = 5.9 cm) versus the range of sepal lengths (7.9 - 4.3 = 3.6 cm; standard deviation 0.83).

Based on the observations made above, and assuming that the high variability in petal size is at least partially contingent on iris species, it seems likely that petal dimension will be more useful in classifying iris samples than sepal dimension. One way of testing that hypothesis, and of generally learning more about the data, is to produce the same descriptive statistics broken down by class (i.e. iris variety). This is achieved using pandas ```DataFrame.groupby()``` method [REF]. The resulting tables appear below. Each table represents one of the four observed features (lengths and widths of petals and sepals), and each column of each table represents one of the three classes (*I. setosa*, *I. versicolor*, and *I. virginica*). The rows contain the same descriptive statistics as in the table above, for each combination of feature and class.


<table>
<tr>
<th> Petal Length </th>
<th> Petal Width </th>
</tr>
<tr>
<td>

<!-- {% Petal Length %} -->

|       |   Iris-setosa |   Iris-versicolor |   Iris-virginica |
|-------|---------------|-------------------|------------------|
| count |         50    |             50    |            50    |
| mean  |          1.46 |              4.26 |             5.55 |
| std   |          0.17 |              0.47 |             0.55 |
| min   |          1    |              3    |             4.5  |
| 25%   |          1.4  |              4    |             5.1  |
| 50%   |          1.5  |              4.35 |             5.55 |
| 75%   |          1.58 |              4.6  |             5.88 |
| max   |          1.9  |              5.1  |             6.9  |



<!-- {% END %} -->

</td>
<td>


<!-- {% Petal Width %} -->

|       |   Iris-setosa |   Iris-versicolor |   Iris-virginica |
|-------|---------------|-------------------|------------------|
| count |         50    |             50    |            50    |
| mean  |          0.25 |              1.33 |             2.03 |
| std   |          0.11 |              0.2  |             0.27 |
| min   |          0.1  |              1    |             1.4  |
| 25%   |          0.2  |              1.2  |             1.8  |
| 50%   |          0.2  |              1.3  |             2    |
| 75%   |          0.3  |              1.5  |             2.3  |
| max   |          0.6  |              1.8  |             2.5  |



<!-- {% END %} -->

</td>
</tr>
<tr>
<th> Sepal Length </th>
<th> Sepal Width</th>
</tr>
<tr>
<td>

<!-- {% Sepal Length %} -->

|       |   Iris-setosa |   Iris-versicolor |   Iris-virginica |
|-------|---------------|-------------------|------------------|
| count |         50    |             50    |            50    |
| mean  |          5.01 |              5.94 |             6.59 |
| std   |          0.35 |              0.52 |             0.64 |
| min   |          4.3  |              4.9  |             4.9  |
| 25%   |          4.8  |              5.6  |             6.22 |
| 50%   |          5    |              5.9  |             6.5  |
| 75%   |          5.2  |              6.3  |             6.9  |
| max   |          5.8  |              7    |             7.9  |



<!-- {% END %} -->

</td>
<td>

<!-- {% Sepal Width %} -->

|       |   Iris-setosa |   Iris-versicolor |   Iris-virginica |
|-------|---------------|-------------------|------------------|
| count |         50    |             50    |            50    |
| mean  |          3.43 |              2.77 |             2.97 |
| std   |          0.38 |              0.31 |             0.32 |
| min   |          2.3  |              2    |             2.2  |
| 25%   |          3.2  |              2.52 |             2.8  |
| 50%   |          3.4  |              2.8  |             3    |
| 75%   |          3.68 |              3    |             3.18 |
| max   |          4.4  |              3.4  |             3.8  |



<!-- {% END %} -->

</td>
</tr>
</table>

The suggestion above regarding the suitability of petal dimensions in classifying iris species is borne out by the class-grouped statistics. Here it can be seen that there is a considerable gap between both the mean petal widths, and the mean petal lengths of *I. setosa* and the other two classes. Looking first at petal length; *I. setosa* shows a mean petal length of 1.46 cm against 4.26 cm and 5.55 cm for *I. versicolor* and *I. virginica* respectively. Examining the minimum and maximum petal lengths for each class confirms that this is a good metric for class separation. The maximum petal length observed in an *I. setosa* specimen is 1.9 cm while the minimum observed in *I. versicolor* and *I. virginica* was 3 cm and 4.5 cm respectively. Petal length alone, therefore, is sufficient to separate *I. setosa* from the other two varieties.

As regards *I. versicolor* and *I. virginica*; there is an approximate 25% range overlap between these two species in terms of petal length as evinced by *I. versicolor*'s third quartile value of 4.6 cm against *I.virginica*'s minimum of 4.5 cm. This demonstrates that while petal length may contribute to the differentiation of theses two species, the separation, if based on this metric alone, will not be perfect.

The case with petal width is similar, albeit less pronounced. Certain identification of *I. setosa* appears to be possible using this metric alone, but the other two species will not be separated with the same certainty. Sepal dimensions don't appear to make a significant contribution to the problem of iris species identification.

<hr>

### Visualisation of Descriptive Statistics

Descriptive statistics, as demonstrated above, can be powerful summarisers of a dataset but the most powerful tool available for EDA is arguably visualisation. The use of some simple charts can provide considerable information more quickly and more intuitively than analysis of the underlying values directly.

#### Histograms

The Seaborn library (REF), which is built on Matplotlib (REF) offers a powerful and flexible interface for data visualisation. The histograms below are generated by applying the ```seaborn.displot()```[REF] method to the long-form iris data.

<!-- {% Stacked Histograms %} -->

![Stacked Histograms](output/histograms_stacked.png)

<!-- {% END %} -->

It is clear from the upper histograms that there is little correlation between sepal dimension and class. The petal length and width histograms, on the other hand, clearly show that there is no overlap between the petal dimensions of *I. setosa* and those of the other two classes. Some overlap is evident between *I. versicolor* and *I. virginica* in terms of petal length and width but, especially in the case of petal width, the overlap is minimal, pointing to a high degree of correlation between the class and those two variables.

#### Boxplots

The boxplots below (generated using [```seaborn.catplot(... kind="box" ...)```](https://seaborn.pydata.org/generated/seaborn.catplot.html)) succinctly encode a wealth of information into a simple chart. The box itself represents the interquartile range, i.e. the distance between the first and the third quartiles — thus representing 50% of the range of values in the dataset if it is normally distributed. The vertical line inside the box represents the median. The 'whiskers' extend to 1.5x the inter-quartile range and any values outside of that range can be considered outliers and are represented by points.

<!-- {% Boxplots %} -->

![Boxplots](output/boxplots.png)

<!-- {% END %} -->

In addition to encoding the structure of the data the boxplots can offer some insight into the problem of classification. It can be seen that neither sepal length nor width alone can be used to distinguish the class of an observation, but *I. setosa* can be identified using either petal length or width. Although none of the observed features is suitable for uniquely identifying *I. versicolor* or *I. virginica*, the bulk of the observations of those two varieties would be identifiable solely using one or other of the petal dimensions.

#### Stripplots

A similar story is told by the stripplot ([```seaborn.stripplot()```](https://seaborn.pydata.org/generated/seaborn.stripplot.html)) below. The less mixing occurring between classes, and the greater range — represented by the vertical spread of the markers — indicates greater separability of those classes.  

<!-- {% Stripplot %} -->

![Stripplot](output/stripplot.png)

<!-- {% END %} -->

As such, the stripplot here appears to indicate that, while either petal width or length are sufficient to identify *I. setosa*, petal length is the clearer indicator. Petal length also appears to come closest to separating *I. versicolor* and *I. virginica*.

#### ECDF (Empirical Cumulative Distribution Function)

The final distribution plot that will be examined here is the ECDF (REF). The plot below was generated using [```seaborn.displot(... kind="ecdf" ...```](https://seaborn.pydata.org/generated/seaborn.displot.html)).

The ECDF plot plots a function which returns, for any particular value, what proportion of the data lies below that value — it is like a cumulative distribution curve. This can give useful insights into the structure of the data that may be less obvious in some of the other distribution plots. The faceted plot below shows the ECDF for each of the four observed features for each iris variety. Vertical dotted red lines are added at the maximum value for each feature so that the overlap, or region of possible misclassification, can be easily identified.

<!-- {% ECDF %} -->

![ECDF](output/ecdf.png)

<!-- {% END %} -->

Examination of the first plot — *Sepal Length* — reveals that all sepal length measurements of *I. versicolor* which are below the maximum sepal length measured on *I. setosa* correspond to a proportion of ~0.4. This means that ~40% of *I. versicolor* samples observed are indistinguishable from *I. setosa* based on sepal length alone. Similarly, almost 80% of *I. virginica* samples overlap with *I. versicolor* in terms of sepal length. Clearly Sepal length is a poor indicator of iris species.

As noted previously, petal dimensions appear to provide the clearest metric for identification of iris species but, contrary to the assumption made above on observation of the stripplot, it is petal width rather than petal length that will probably provide the fewest misclassifications. This is confirmed by examining the bottom two ecdf plots. Note that the petal length overlap between *I. versicolor* and 
*I. virginica* accounts for almost 20% of the sample space, whereas, for petal width, the overlap covers less than 10%. 

Recall from the [descriptive statistics](#descriptive-statistics) section that the maximum value for *I. versicolor* petal width is 1.8 cm. This can be confirmed by querying the dataframe: ```np.max(iris[iris["class"]=="Iris-versicolor"]["Petal Width"])```. Another query, this time for all observations with a petal width value of 1.8 (```iris[iris["Petal Width"] == 1.8]```) returns the following result:


<!-- {% Petal Width = 1.8 %} -->

|     |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width | class           |
|-----|----------------|---------------|----------------|---------------|-----------------|
|  70 |            5.9 |           3.2 |            4.8 |           1.8 | Iris-versicolor |
| 103 |            6.3 |           2.9 |            5.6 |           1.8 | Iris-virginica  |
| 107 |            7.3 |           2.9 |            6.3 |           1.8 | Iris-virginica  |
| 108 |            6.7 |           2.5 |            5.8 |           1.8 | Iris-virginica  |
| 116 |            6.5 |           3   |            5.5 |           1.8 | Iris-virginica  |
| 123 |            6.3 |           2.7 |            4.9 |           1.8 | Iris-virginica  |
| 125 |            7.2 |           3.2 |            6   |           1.8 | Iris-virginica  |
| 126 |            6.2 |           2.8 |            4.8 |           1.8 | Iris-virginica  |
| 127 |            6.1 |           3   |            4.9 |           1.8 | Iris-virginica  |
| 137 |            6.4 |           3.1 |            5.5 |           1.8 | Iris-virginica  |
| 138 |            6   |           3   |            4.8 |           1.8 | Iris-virginica  |
| 149 |            5.9 |           3   |            5.1 |           1.8 | Iris-virginica  |

<!-- {% END %} -->

## Relationships

### Correlation
1. Covariance
2. ρ (Pearson correlation)
3. Variability due to codependence / independent variability

### Visualisation of Relationships


<!-- {% Pairplot %} -->

![Pairplot](output/pairplot.png)

<!-- {% END %} -->


<!-- {% Classification Petal %} -->

<img src="output/scatter_petal.png" height=500>

<!-- {% END %} -->


<!-- {% Classification Sepal %} -->

<img src="output/scatter_sepal.png" height=500>

<!-- {% END %} -->




### Separation improvement

<!-- {% Classification Area %} -->

<img src="output/scatter_area.png" height=500>

<!-- {% END %} -->

1. Dimensionality reduction
    1. LDA
    2. PCA
    3. Area


## Further Study

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

https://stackoverflow.com/a/59852474 (markdown columns)
https://pypi.org/project/tabulate/ (tablefmt option in pandas.DataFrame.to_markdown())
https://seaborn.pydata.org/tutorial/data_structure.html --- long vs wide formats
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html --- dataframe.melt()
https://www.opentechguides.com/how-to/article/pandas/193/index-slice-subset.html --- dataframe slicing
https://towardsdatascience.com/7-points-to-create-better-histograms-with-seaborn-5fb542763169 --- histograms
https://stackoverflow.com/a/31688467 --- On setting titles on facetgrids
https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-areas.html --- LDA and a trick
https://www.machinecurve.com/index.php/2020/05/05/how-to-create-a-confusion-matrix-with-scikit-learn/ --- confusion matrix

https://stackoverflow.com/a/29814281 --- facetgrid title

https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480

https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51

https://data.library.virginia.edu/understanding-empirical-cumulative-distribution-functions/

https://seaborn.pydata.org/generated/seaborn.ecdfplot.html