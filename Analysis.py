# Programming and Scripting Final Project - 2022

# This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code to investigate it.
# The programme must output a summary of each variable to a single text file, Save a histogram of each variable to png files and output a scatterplot of each pair of variables. 
# Perform any other analysis you think is appropriate. 

# Author: Jamie Tohall


#### Importing relevant modules ####

import pandas as pd # To read in Iris.csv file which contains the Iris Data Set
import seaborn as sns # To use historgrams, scatterplots, and pairplots
import matplotlib.pyplot as plt # To create plots
import numpy as np 


#### Read in Iris Data Set ####

# Will read in the Iris data set from the csv file I downloaded and saved ontop my desktop
Irisdata = pd.read_csv("Iris.csv.txt")


#### Preprocessing the Data Set ####

# The following commands will test the data set I had downloaded was read in properly and also that the information was correct. It will also give me an insight to the data.

# This will return the number of lines and columns in the data set table. Result is 150 lines and 5 columns (150,5)
print(Irisdata.shape)

# Will print the top 5 lines of the table, including the headers. The default value of the function is 5 lines of no exact command is given and I didn't specify a number.
print (Irisdata.head())

# I will also print a 15 line sample of the data, this will print 15 random lines.
print (Irisdata.sample(15))

# The following command will output all the columns from the dataset in list form.
print (Irisdata.columns)

# This will print a statistical insight of each of the four variable in the Data set including the mean values, standard deviation, minimum values and maximum values.
print (Irisdata.describe())

# I then checked the balance of the data input, counting how many times each species was counted.
print (Irisdata["species"].value_counts()) 