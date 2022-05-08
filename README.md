# Pands Project #
<br/>

#### Author: Jamie Tohall
#### Student Number: G00411380
<br/>

#### Module: Programming and Scripting
#### Lecturer: Andrew Beattie
#### Submission Date: 29th April 2022


<br/>


## Project Objective ##
<br/>

> This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code (in Python) to investigate it. An
> online search for information on the data set will convince you that many people have investigated it previously. You are expected to be able to break this project 
> into several smaller tasks that are easier to solve, and to plug these together after they have been completed. 

<br/>

## Fisher's Iris Data Set ##
<br/>

 ![picture alt](https://miro.medium.com/max/700/1*uo6VfVH87jRjMZWVdwq3Vw.png)
 <br/>
 
Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis'. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.<br/>
The iris data set is widely used as a beginner's dataset for machine learning purposes, often known as the 'Hello world' in the field of data science. The Data set is used in data mining, classification and clustering examples and to test algorithms. 

<br/>

## Process of Data Analysis ##
<br/>

### Importing Modules ###

I Imported three modules in total; <br/>

**Matplotlib** - Matplotlib is a low level graph plotting library in python that serves as a visualization utility. One of the greatest benefits of visualization is that it allows visual access to huge amounts of data in easily digestible visuals. Matplotlib consists of several plots like line, bar, scatter, histogram etc. I used Matplotlib in my analysis to create Histograms, Overlapping Histograms, Scatterplots, a Scatterplot Matrix and a Heatmap. <br/>

**Seaborn** - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. I used seaborn to create Overlapping Histograms, Scatterplots, a Scatterplot Matrix and a Heatmap. <br/>

**Pandas** - Pandas is an open-source library that is made mainly for working with relational or labelled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. I used Pandas to read in the Iris data set CSV file.

<br/>

### Reading in the Iris Data Set ###

I began by searching online for the Iris Data Set. I found the full data code on pyhub01.gitbook.io, so I copied the code and pasted it to a text file and titled it 'iris'. I then changed the suffix of the text file from txt to csv, this changed the format from plain text to a table. I then saved the csv file to a folder on my homepage titled 'Pands Project', So I was then able to access the file through Visula Studio Code. I then opened the csv file in read format so I could start to analyse the data. ```Irisdata = pd.read_csv("Iris.csv").```

Link to Iris Data Set: https://pyhub01.gitbook.io/python-complete-tutorial/data-mining-and-machine-learning/iris-data-set

<br/>

### Creating a text file for Summary Output ###

As outlined in the project instructions, I was to create a single text file where I could output a summary of each variable from the Data Set. I created a text file titled 'Summary of Variables', and opened it in write format ```with open ("Summary_of_Variables", "w") as f:```. I wrote the title of the text file ```f.write("Summary of Variables from The Iris Data Set")```, and I used '\n' to create a new space under the title ```f.write("\n\n")```.  

<br/>

###  Preprocessing the Data Set ###

Before I began to analyse the Data set I preprocessed it. Using a number of different commands to gather information, such as the column size, Column index and the statistical insight to each variable.

* **Shape**<br/>
```(150, 5)```

* **Head**
``` 
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```

* **Sample**
```

```


* **Columns**
```
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
       'species'],
      dtype='object')
```

* **Describe**
```
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
```

* **Value Counts**
```
Displaying the number of times a particular data has occured
setosa        50
versicolor    50
virginica     50
Name: species, dtype: int64
```

* **Sum, Mean & Median**
```
Sum: 876.5 
Mean: 5.843333333333335 
Median: 5.8
```
```
Sum: 458.1 
Mean: 3.0540000000000007 
Median: 3.0
```
```
Sum: 563.8 
Mean: 3.7586666666666693 
Median: 4.35
```
```
Sum: 179.8 
Mean: 1.1986666666666672 
Median: 1.3
```

<br/>

### Histograms ###
<br/>

### Overlapping Histograms ###
<br/>

### Scatterplots ###
<br/>

### Scatterplot Matrix ###
<br/>

### Conclusion ###

<br/>



## References ##

<br/>

**[1]** 3.6.10.4. Plot 2D views of the iris dataset — Scipy lecture notes (scipy-lectures.org)
https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html <br/>
**[2]** Exploratory Data Analysis : Iris Dataset | by Pranshu Sharma | Analytics Vidhya | Medium 
https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda <br/>
**[3]** How To Make Histogram in Python with Pandas and Seaborn? - Python and R Tips (cmdlinetips.com)
https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/ <br/>
**[4]** How to Write to Text File in Python (pythontutorial.net)
https://www.pythontutorial.net/python-basics/python-write-text-file/ <br/>
**[5]** Introduction to Pandas in Python - GeeksforGeeks 
https://www.geeksforgeeks.org/introduction-to-pandas-in-python/ <br/>
**[6]** iris data set - Python complete tutorial (gitbook.io)
https://pyhub01.gitbook.io/python-complete-tutorial/data-mining-and-machine-learning/iris-data-set <br/>
**[7]** Iris flower data set - Wikipedia 
https://en.wikipedia.org/wiki/Iris_flower_data_set <br/>
**[8]** Linear Regression in Python – Real Python 
https://realpython.com/linear-regression-in-python/ <br/>
**[9]** Linear Regression using Iris Dataset — ‘Hello, World!’ of Machine Learning | by Darryl See Wei Shen | Analytics Vidhya | Medium 
https://medium.com/analytics-vidhya/linear-regression-using-iris-dataset-hello-world-of-machine-learning-b0feecac9cc1 <br/>
**[10]** Machine Learning in Python: Iris Classification -- Part 3 - Bing video 
https://www.bing.com/videos/search?q=iris+data+set+in+python&&view=detail&mid=5A63C8BAA51DABB6C4715A63C8BAA51DABB6C471&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Diris%2Bdata%2Bset%2Bin%2Bpython%26FORM%3DHDRSC4 <br/>
**[11]** Overlapping Histograms with Matplotlib in Python - GeeksforGeeks 
https://www.geeksforgeeks.org/overlapping-histograms-with-matplotlib-in-python/ <br/>
**[12]** Python - Basics of Pandas using Iris Dataset - GeeksforGeeks 
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ <br/>
**[13]** Python for Data Science - Exploratory Data Analysis - IRIS Dataset - Notepub 
https://notepub.io/notes/programming-languages/python-for-data-science/python-for-data-science-exploratory-data-analysis-iris-dataset/ <br/>
**[14]** Seaborn (python-graph-gallery.com) 
https://python-graph-gallery.com/seaborn/<br/>
**[15]** Seaborn Heatmap - A comprehensive guide - GeeksforGeeks 
https://www.geeksforgeeks.org/seaborn-heatmap-a-comprehensive-guide/ <br/>
**[16]**  Seaborn Scatter Plot - Tutorial and Examples (stackabuse.com) 
https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/ <br/>
**[17]** seaborn.heatmap — seaborn 0.11.2 documentation (pydata.org) 
https://seaborn.pydata.org/generated/seaborn.heatmap.html <br/>
**[18]** seaborn.pairplot — seaborn 0.11.2 documentation (pydata.org) 
https://seaborn.pydata.org/generated/seaborn.pairplot.html <br/>
**[19]** seaborn: statistical data visualization — seaborn 0.11.2 documentation (pydata.org)
http://seaborn.pydata.org/ <br/>
**[20]** ValueError: I/O operations on closed file (stechies.com)
https://www.stechies.com/valueerror-io-operations-closed-file/ <br/>
**[21]** What, When & How of Scatterplot Matrix in Python - Data Analytics (vitalflux.com) 
https://vitalflux.com/what-when-how-scatterplot-matrix-pairplot-python/ <br/>
**[22]** What, When & How of Scatterplot Matrix in Python - Data Analytics (vitalflux.com) 
https://vitalflux.com/what-when-how-scatterplot-matrix-pairplot-python/ <br/>

