# Programming and Scripting Final Project - 2022

# This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code to investigate it.
# The programme must output a summary of each variable to a single text file, Save a histogram of each variable to png files and output a scatterplot of each pair of variables. 
# Perform any other analysis you think is appropriate. 

# Author: Jamie Tohall


####### Importing relevant modules #######

import pandas as pd # To read in Iris.csv file which contains the Iris Data Set
import seaborn as sns # To use historgrams, scatterplots, and pairplots
import matplotlib.pyplot as plt # To create plots
import numpy as np 


####### Read in Iris Data Set #######

# Will read in the Iris data set from the csv file I downloaded and saved ontop my desktop
Irisdata = pd.read_csv("Iris.csv")


####### Creating a text file to output the variable summary #######

# I created a text file. 
text = open ("Summary_of_Variables", "w")
Irisdata.head()
  

####### Preprocessing the Data Set #######

# The following commands will test that the data set I downloaded was read in properly and also that the information was correct. It will also give me an insight to the data set table and its information.

# This will return the number of lines and columns in the data set table. Result is 150 lines and 5 columns (150,5)
print(Irisdata.shape)

# After each command I printed a space, to make the final output look neater and easier to read.
print (' ')

# Will print the top 5 lines of the table, including the headers. The default value of the function is 5 lines of no exact command is given and I didn't specify a number.
print (Irisdata.head())
print (' ')

# Similarly, I will also print a 15 line sample of the data, this will print 15 random lines.
print (Irisdata.sample(15))
print (' ')

# The following command will output all the columns from the dataset in list form.
print (Irisdata.columns)
print (' ')

# This will print a statistical insight of each of the four variable in the Data set including the mean values, standard deviation, minimum values and maximum values.
print (Irisdata.describe())
print (' ')

# I then checked the balance of the data input, counting how many times each species was counted.
print (Irisdata["species"].value_counts()) 
print (' ')



####### Data Analysis #######

# I will start to analyse the Iris set Data using histograms, scatter plots and pairplots to display each of the variables.

# The first histogram will display the Sepal Width for all three species.

plt.figure(figsize = (10, 7))
x = Irisdata.sepal_width  
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Sepal Width for all Species")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Count")
plt.savefig ("Sepal Width for all Species")
plt.show()

plt.figure(figsize = (10, 7))
x = Irisdata.sepal_length 
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Sepal Length for all Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.savefig ("Sepal Length for all Species")
plt.show()

plt.figure(figsize = (10, 7))
x = Irisdata.petal_width
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Petal Width for all Species")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Count")
plt.savefig ("Petal Width for all Species")
plt.show()

plt.figure(figsize = (10, 7))
x = Irisdata.petal_length
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Petal Length for all Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Count")
plt.savefig ("Petal Length for all Species")
plt.show()