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
Iris is a genus of 260–300 species of flowering plants with showy flowers. It takes its name from the Greek word for a rainbow, which is also the name for the Greek goddess of the rainbow, Iris. Some authors state that the name refers to the wide variety of flower colors found among the many species. As well as being the scientific name, iris is also widely used as a common name for all Iris species, as well as some belonging to other closely related genera. 
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

Before I began to analyse the Data set I preprocessed it. Using a number of different commands to gather information, such as the column size, column index and the statistical insight to each variable. Each command output is then sent to the text file titled "Summary of Variables from the Iris Data Set". To direct the output of the commands to the text file I wrote ```print (Irisdata.shape, file = open ("Summary_of_Variables", "a"))```. While first writing my code I wrote "w" at the end of this command instead of "a", this would then rewrite over anything I had previously in my text file, so I could never have more than one command output there at one time. However, after some very useful feedback in our class teams discussion, I was shown that after the initial commmand is entered with "w", every command after is added with "a", which doesn't overwrite the previous enteries. <br/>
For most of the commands below, they were all similar to write (Apart from Sum, Mean and Median). With shape for example, I firstly wrote a title for the command entry, and sent the output to the text file ```print ("Number of lines and columns in Iris Data Set", file = open ("Summary_of_Variables", "a"))```. In the next line I would execute the Shape command within the data set, which I saved as 'Irisdata', and output the results to the text file ```print (Irisdata.shape, file = open ("Summary_of_Variables", "a"))```. Finally, I printed a new line, so there was space between this entry and the next, making the text file easier to read ```print ("\n", file = open ("Summary_of_Variables", "a"))```.,br/>
With the Sum, Mean & Median command it was formatted a little differently. To calcualte the Sum, Mean and Median of the Sepal Length for example, I again started with a header for the command input in the text file ```print ("Sum, Median and Mean of Sepal Length", file = open ("Summary_of_Variables", "a")). I then calculated the sum, by again referencing my data 'Irisdata', and entering the column labelled "sepal length" as the data that I wish to be calculated. I repeated this for the mean and the Median.
```
sum_data = Irisdata["sepal_length"].sum() 
mean_data = Irisdata["sepal_length"].mean() 
median_data = Irisdata["sepal_length"].median()
```
I then directed the ouput to the text file, making sure to place a \n after each entry so it was formatted as a list, rather than it all being printed on the one line ```print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, file =open("Summary_of_Variables", "a"))```
again, I would then print a new line after this entry, as to neatly format the text file ```print ("\n", file = open ("Summary_of_Variables", "a"))```<br/>
I would repeat the same code above for the Sepal Width, Petal Length and Petal Width. 

<br/>

* **Shape**<br/>
The shape command will output the number of lines and columns in the data set. From the output below we can see that there are 150 lines of data and 5 columns. <br/>

```(150, 5)```

<br/>

* **Columns**<br/>
The columns command will give us an index of all the column headers in list form. As you can see below the columns are Sepal Length, Sepal Width, Petal Length and Petal Width. 
```
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
       'species'],
      dtype='object')
```

<br/>

* **Head**<br/>
The 'head' command will output the first 5 lines of the Data set including the headers. The amount of lines can be edited to more or less, however 5 lines is the deafault setting if no particular number is commanded. This will give us an insight to how the table is formatted, we can also see the four variables labelled at the top: Sepal length, Sepal Width, Petal Length and Petal Width. The last column is the different type of species, and we can see that Setosa is the first of the three species to be labelled. 

``` 
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```

<br/>

* **Sample**<br/>
From the sample command we will receive an output of 15 random lines from the date set underneath the column headers. Each time this command is executed, a different sample is outputted. Again, we can edit the number of sample lines we wish to see, I chose 15 lines as I thought it was a large enough number to gather some insight of the data recorded. From the sample lines outputted we can see the three different species of Iris are Virginica, Setosa and Versicolor. In total we have 6 lines of data for Setosa, 6 lines for Virginica, and 3 lines for Versicolor. I think this is a reasonable sample number for each species as it will be unlikely that I would get an even 5 lines for each of the species. If the output was heavily uneven or there was a species missing from the sample then I would execute the command again. On the left of the table we see a column of different numbers, these are the line numbers which tell us where on the table the sample line is from. <br/>
If I were to only analyse the data given below, I would assume that the Setosa was the smaller of the three species given the petal width of the Setosa on average is only 0.2, and its largest petal length counted is 1.6. The smallest petal length for the Versicolor is 3.6, and the smallest for the Virginica is 5.5, which shows a 2cm differernce between the Setosa's largest petal length and the next species smallest petal length. When we look at sepal width however, its the Versicolor with the smaller numbers, Setosa then seems to have the smaller Sepal Lengths. The Versicolor and Virginica species seem to be more similar in size, however the Virginica is recording the larger numbers across all the columns. It will be interesting to see if this short analysis of a sample of data is still accurate when analysing the full data set.

```
     sepal_length  sepal_width  petal_length  petal_width     species
64            5.6          2.9           3.6          1.3  versicolor
102           7.1          3.0           5.9          2.1   virginica
103           6.3          2.9           5.6          1.8   virginica
131           7.9          3.8           6.4          2.0   virginica
2             4.7          3.2           1.3          0.2      setosa
144           6.7          3.3           5.7          2.5   virginica
39            5.1          3.4           1.5          0.2      setosa
29            4.7          3.2           1.6          0.2      setosa
116           6.5          3.0           5.5          1.8   virginica
125           7.2          3.2           6.0          1.8   virginica
4             5.0          3.6           1.4          0.2      setosa
65            6.7          3.1           4.4          1.4  versicolor
27            5.2          3.5           1.5          0.2      setosa
17            5.1          3.5           1.4          0.3      setosa
89            5.5          2.5           4.0          1.3  versicolor
```

<br/>

* **Value Counts**<br/>
We can count the occurance of each species in the data set, which will also confirm the balance of the data if correct. We can see from the output below that each species of Iris was counted 50 times, and there are 150 lines in the data set, so each species has been counted equally. 

```
setosa        50
versicolor    50
virginica     50
Name: species, dtype: int64
```
<br/>

* **Sum, Mean & Median**<br/>
I then calcualted the sum, mean and median of each of the columns; petal length, petal width, sepal length and sepal width, including all three species. From this data we can begin to gather some basic information from the data set, for example we can cross reference the mean of each of the categories to the mean of the species result, to better classify the difference species. 

Sepal Length
```
Sum: 876.5 
Mean: 5.843333333333335 
Median: 5.8
```
Sepal Width
```
Sum: 458.1 
Mean: 3.0540000000000007 
Median: 3.0
```
Petal Length
```
Sum: 563.8 
Mean: 3.7586666666666693 
Median: 4.35
```
Petal Width
```
Sum: 179.8 
Mean: 1.1986666666666672 
Median: 1.3
```

<br/>

* **Describe**<br/>
Describe will output similar results to the sum, mean & median command above, however it will give us some more information, such as the total count of each category, the standard deviation, minimum values and maximum values. It will also output all of the information in a table format. This table will be a good referencing point when analysing each of the different species and their measurements in each category.
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
<br/>

### Histograms ###
I created four histograms in total, each one showing the data of all the three species in each of the categories; Petal Length, petal width, Sepal Length and Sepal Width. Each histogram gives us more of a visual insight to the results of each category and its numerical data.
<img src="https://user-images.githubusercontent.com/98059109/167313582-0416ba9f-6ae5-4347-a537-b45bc9ee8f1f.png">
<br/>
**1. Petal Length for all Species**<br/>
When viewing the first histogram I can see there is a gap in the petal length between 2cm and 3cm. The count of the petal length also seems to be quite varied, with a large count around the 1.5cm mark. 

**2. Petal Width for all Species**<br/>
Again, we can see a gap towards the left hand side of the histogram, between the 0.75cm and the 1cm mark. There is also quite a large count toward the lower end of the petal size. We could assume at this point that the gap in this histogram (and histogram 1) could be the difference between the Setosa species of iris, and the other two species Versicolor and Virginica. However this would be mostly speculation at this point as we have not yet looked at the results of each individual species in each category. 

**3. Sepal Length for all Species**<br/>
The overall count of the sepal seems to be quite varied, with no noticeably large count, unlike the petal length. The count seems to be evenly distributed but with no obvious pattern, making us unable to differentiate between the species and their sepal length.

**4. Sepal Width for all Species**<br/>
The histogram for Sepal with is giving us a triangle result, were the data count on the smaller and larger end of the sepal size are smaller, and it becomes larger in the middle, over the 3cm mark. Again it is difficult to distinguish the Iris species here without making assumptions.

<br/>

### Overlapping Histograms ###
The overlapping histograms will show us the same data as the histograms, however it will also show us the result of each species of iris on the histogram. 
<img src="https://user-images.githubusercontent.com/98059109/167313930-62e8eb3b-4e16-430d-92a5-3efae8a30429.png">
<br/>
**1. Petal Length**<br/>
This Overlapping histogram confirms the theory I had when looking at the previous histogram for petal length. That the gap in the petal lengths are the difference between the smaller Setosa species and the Versicolor and Virginica species. This histogram also shows us that the cluster of data on the larger end of the petal length isn't as mixed as I would have thought. Virginica Is at the larger end of the scale, and Versicolor is just below. 

**2. Petal Width**<br/>
This histogram shows us similar results to the petal length image. Again, all the Setosa data is at the lower end of the petal width size, with a gap between it and the other two species of Iris. Virginica once again is at the larger end of the scale, and Versicolor is just below Virginica. 

**3. Sepal Length**<br/>
When it comes to the sepal length, we can see that the results of each species overlap a bit more. We can even see an overlap in the middle between the larger setosa sepal length and the smaller Virginica Sepal length. The results show us what we otherwise would have assumed, that Setosa was on the smaller end of the Sepal length and Virginica is on the larger end, with Versicolor in the middle. 

**4. Sepal Width**<br/>
When looking at the overlapping histogram for Sepal Width, at first glance it looks like a mistake! Setosa seems to have the average larger Sepal width of the three species. Versicolor is on the smaller side instead of the middle unlike the previous three categories, and Virginica is cushioned in the middle, with quite alot of overlap on either end.

<br/>

### Scatterplots ###
I created six scatterplots in total, one of each pair of variables. Petal Length v Petal Width, Petal Length v Sepal length, Petal Length v Sepal Width, Petal Width v Sepal Width, Sepal Length v Petal Width and Sepal Length v Sepal Width. 
<img src="https://user-images.githubusercontent.com/98059109/167314314-eca66a04-e049-441a-b110-120207ca000b.png">
<br/>
As you can see from all of the six scatterplots above, there is a noticeable difference between the Setosa results in all of the variables, and the Versicolor and Virginica results. Versicolor and Virginica again are alot closer in size, however Versicolor on average is slightly smaller than Virginica.

<br/>

### Scatterplot Matrix ###
I created a scatterplot matrix as I thought it was a nice visualisation tool to easily explore any trends in the data. It shows the same results as our overlapping histograms and the scatterplots, although some of the scatterplots in the matrix are flipped and inverted to the ones we previously created, as it also shows the cateogries on different axies. This is a great way to look at data from a different angle (literally) and see if there are any breakthough results that we previously missed.

<img src="https://user-images.githubusercontent.com/98059109/167313293-2fbb8866-7f14-448b-82b9-33dfd2428527.png" width=80% height=80%>
<br/>
Looking at the Matrix and all the 12 scatterplots, I still see an obvious difference between the Setosa data and the closer virginica and Versicolor data.

<br/>
<br/>

### Heatmap ###
A heatmap is a data visualization technique where colours represent how a value of interest changes with the values of other variables. It is a two-dimensional graphical representation of data with values encoded in colours, thereby giving a simplified, insightful, and visually appealing view of information.

<img src="https://user-images.githubusercontent.com/98059109/167313177-ac3a199d-826a-4c05-8d97-202412427fab.png" width=70% height=70%>
<br/>
When we analyse the heatmap, we can see that the Sepal Length and Sepal Width are slightly correlated with each other.

<br/>
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

