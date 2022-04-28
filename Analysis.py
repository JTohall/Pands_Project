# Programming and Scripting Final Project - 2022
# Author: Jamie Tohall
# Submission date: 29th April 2022

################# Importing relevant modules #################

import pandas as pd # To read in Iris.csv file which contains the Iris Data Set
import seaborn as sns # To create histograms and scatterplots
import matplotlib.pyplot as plt # To create histograms and scatterplots


################# Read in Iris Data Set #################

# I read in the Iris data set from the file I downloaded and saved ontop my desktop. I downloaded the data as a txt file, and changed the suffix to .csv
# I downloaded the data from - "https://pyhub01.gitbook.io/python-complete-tutorial/data-mining-and-machine-learning/iris-data-set"
Irisdata = pd.read_csv("Iris.csv")


################# Creating a text file to output the Variable Summary #################

# I created a text file titled 'Summary of Variables', and opened it in write format. I began by writing the Title of the file and then using "\n\n" to create a new line
# below the header, so the file contents don't look messy and difficult to read.
with open ("Summary_of_Variables", "w") as f:
   f.write("Summary of Variables from The Iris Data Set")
   f.write("\n\n")
  

################# Preprocessing the Data Set #################

# The following commands will test that the data set I downloaded was read in properly and also that the information was correct. 
# It will also give me an insight to the Iris Data Set and its information. All information from each command will then
# be directed to the text file "Summary of Variables".


# This will return the number of lines and columns in the data set table. Result is 150 lines and 5 columns (150,5)
print ("Number of lines and columns in Iris Data Set", file = open ("Summary_of_Variables", "a")) 
# Firstly, I created a title for the results and used 'file=open' to output the title to the text file. 
print (Irisdata.shape, file = open ("Summary_of_Variables", "a"))
# This is the command used to count the number of lines and columns (shape), and again I output the results of the command to the txt file.
print ("\n", file = open ("Summary_of_Variables", "a"))
# After each command I printed a new line "\n" to make the final output neater and easier to read.


# Will print the top 5 lines of the table, including the headers. The default value of the function is 5 lines if no exact command is given and I didn't specify a number.
print ("Preview of the top 5 Lines from the Data Set", file = open ("Summary_of_Variables", "a")) # Created a title for the command
print (Irisdata.head(), file = open ("Summary_of_Variables", "a")) # 'head' Command exectuted and output sent to txt file
print ("\n", file = open ("Summary_of_Variables", "a")) # New line created 


# Similarly, I will also print a 15 line sample of the data, this will print 15 random lines.
print ("A random sample of 15 lines from the Data Set", file = open ("Summary_of_Variables", "a")) # Command title
print (Irisdata.sample(15), file = open ("Summary_of_Variables", "a")) # 'Sample' command executed
print ("\n", file = open ("Summary_of_Variables", "a")) # New line


# The following command will output all the columns from the dataset in list form.
print ("An Index of all the Columns", file = open ("Summary_of_Variables", "a")) # Command title
print (Irisdata.columns, file = open ("Summary_of_Variables", "a")) # 'Columns' command executed
print ("\n", file = open ("Summary_of_Variables", "a")) # New line


# This will print a statistical insight of each of the four species in the Data set including the mean values, standard deviation, minimum values and maximum values.
print ("Statistical Insight", file = open ("Summary_of_Variables", "a")) # Command title
print (Irisdata.describe(), file = open ("Summary_of_Variables", "a")) # 'Describe' command executed
print ("\n", file = open ("Summary_of_Variables", "a")) # New line


# I then checked the balance of the data input, counting how many times each species was counted.
print ("Displaying the number of times a particular data has occured", file = open ("Summary_of_Variables", "a")) # Command title
print (Irisdata["species"].value_counts(), file = open("Summary_of_Variables", "a")) # Species 'Value count' command executed
print ("\n", file = open ("Summary_of_Variables", "a")) # New line


# Calculating Sum, Mean and Median of the Sepal Length
print ("Sum, Median and Mean of Sepal Length", file = open ("Summary_of_Variables", "a"))
# Title for the Sepal Length calculations, sent to the txt file. 
sum_data = Irisdata["sepal_length"].sum() # Calculates the sum of the sepal length data
mean_data = Irisdata["sepal_length"].mean() # Calculates the mean of the sepal length data
median_data = Irisdata["sepal_length"].median() #Calculates the median of the sepal length data
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, file =open("Summary_of_Variables", "a"))
# Prints the results, each to a new line, and sends them to the text file
print ("\n", file = open ("Summary_of_Variables", "a")) # New line added

# Sum, Mean and Median of Sepal Width 
# This command and the following two are the same as above, only changing the variable
print ("Sum, Median and Mean of Sepal Width", file = open ("Summary_of_Variables", "a"))
sum_data = Irisdata["sepal_width"].sum()
mean_data = Irisdata["sepal_width"].mean()
median_data = Irisdata["sepal_width"].median()
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, file =open("Summary_of_Variables", "a"))
print ("\n", file = open ("Summary_of_Variables", "a"))

# Sum, Mean and Median of Petal Length
print ("Sum, Median and Mean of Petal Length", file = open ("Summary_of_Variables", "a"))
sum_data = Irisdata["petal_length"].sum()
mean_data = Irisdata["petal_length"].mean()
median_data = Irisdata["petal_length"].median()
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, file =open("Summary_of_Variables", "a"))
print ("\n", file = open ("Summary_of_Variables", "a"))

# Sum, Mean and Median of Petal Width
print ("Sum, Median and Mean of Petal Width", file = open ("Summary_of_Variables", "a"))
sum_data = Irisdata["petal_width"].sum()
mean_data = Irisdata["petal_width"].mean()
median_data = Irisdata["petal_width"].median()
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, file =open("Summary_of_Variables", "a"))
print ("\n", file = open ("Summary_of_Variables", "a"))


################# Data Analysis #################

# I will start to analyse the Iris set Data using histograms, overlapping histograms, scatterplots and a Heatmap.


################# Histograms #################

# The first histogram will display the Sepal Width for all three species.
plt.figure(figsize = (10, 7)) # Using matplotlib to create the histogram, and defining the figure size
x = Irisdata.sepal_width # The Sepal Width data from the data set is now defined as 'x'
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black") 
# Establishing the data for the histogram, amount of bins, colour, and I added an edge colour to make the histogram data clearer 
plt.title("Sepal Width for all Species") # Title of the histogram
plt.xlabel("Sepal Width (cm)") # Labelling the X axis
plt.ylabel("Count") # Labelling the Y axis
plt.savefig ("Histogram - Sepal Width for all Species") # Saving the figure and naming it

# Shows Sepal length for all three species
plt.figure(figsize = (10, 7))
x = Irisdata.sepal_length 
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Sepal Length for all Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.savefig ("Histogram - Sepal Length for all Species")

# Shows Petal width for all three species
plt.figure(figsize = (10, 7))
x = Irisdata.petal_width
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Petal Width for all Species")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Count")
plt.savefig ("Histogram - Petal Width for all Species")

# Shows petal length for all three species
plt.figure(figsize = (10,7))
x = Irisdata.petal_length
plt.hist(x, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Petal Length for all Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Count")
plt.savefig ("Histogram - Petal Length for all Species")


################# Overlapping Histograms  #################

# This Histogram will show the Sepal Length for all three species and display them on the same figure. This will give a better
# view to the correlation of each species sepal length.
# Using seaborn to create the histogram, defining the data input and the figure height
sns.FacetGrid(Irisdata, hue="species", height=5)\
   .map(sns.distplot, "sepal_length")\
   .add_legend() # Adding a legend to easily distinguish each species
plt.title("Sepal length") # Creating a title for the histogram
plt.savefig("Overlapping Histogram - Sepal Length") # Saving the figure and naming it

# Overlapping histogram showing the Sepal Width of all three Species
sns.FacetGrid(Irisdata, hue="species", height=5)\
   .map(sns.distplot, "sepal_width")\
   .add_legend();
plt.title("Sepal Width")
plt.savefig("Overlapping Histogram - Sepal Width")

# Overlapping histogram showing the Petal Length of all three Species
sns.FacetGrid(Irisdata, hue="species", height=5)\
   .map(sns.distplot, "petal_length")\
   .add_legend();
plt.title("Petal Length")
plt.savefig("Overlapping Histogram - Petal Length")

# Overlapping histogram showing the Petal Width of all three Species
sns.FacetGrid(Irisdata, hue="species", height=5)\
   .map(sns.distplot, "petal_width")\
   .add_legend();
plt.title("Petal Width")
plt.savefig("Overlapping Histogram - Petal Width")


################## Scatterplots #################

# Scatterplots are a great visual tool for classifying a large data set and are also easy to understand and to categorise information

# Scatterplot to show correlation of Sepal Length & Sepal Width for each Species
plt.figure(figsize=(10,10),dpi=100) # Using matplotlib to create the scatterplot, and defining the figure size
sns.set_style("whitegrid") # Using seaborn to create a white grid background
sns.scatterplot(x='sepal_length', y='sepal_width',data= Irisdata, hue='species') # Defining the X and Y axis, data input and hue will categorise the species column.
plt.savefig("Scatterplot - Sepal Length v Sepal Width") # Saving the figure and naming the png image.

# Showing the correlation of Petal Length & Petal Width for each Species
plt.figure(figsize=(10,10),dpi=100)
sns.set_style("whitegrid")
sns.scatterplot(x='petal_length', y='petal_width',data= Irisdata, hue='species')
plt.savefig("Scatterplot - Petal Length v Petal Width")

# Showing the correlation of Sepal Length & Petal Width for each Species
plt.figure(figsize=(10,10),dpi=100)
sns.set_style("whitegrid")
sns.scatterplot(x='sepal_length', y='petal_width',data= Irisdata, hue='species')
plt.savefig("Scatterplot - Sepal Length v Petal Width")

# Showing the correlation of Petal Length & Sepal Width of each Species
plt.figure(figsize=(10,10),dpi=100)
sns.set_style("whitegrid")
sns.scatterplot(x='petal_length', y='sepal_width',data= Irisdata, hue='species')
plt.savefig("Scatterplot - Petal Length v Sepal Width")

# Showing the correlation of Petal Length & Sepal Length of each Species
plt.figure(figsize=(10,10),dpi=100)
sns.set_style("whitegrid")
sns.scatterplot(x='petal_length', y='sepal_length',data= Irisdata, hue='species')
plt.savefig("Scatterplot - Petal Length v Sepal Length")

# Showing the correlation of Petal Width & Sepal Width of each Species
plt.figure(figsize=(10,10),dpi=100)
sns.set_style("whitegrid")
sns.scatterplot(x='petal_width', y='sepal_width',data= Irisdata, hue='species')
plt.savefig("Scatterplot - Petal Width v Sepal Width")


################## Scatterplot Matrix #################

# A scatterplot matrix is a grid of scatterplots where each scatterplot in the grid is created between different combinations
# of Variables. A Scatterplot matrix is a great tool for assessing the pairwise relationship between two or more variables.

# Using seaborn module to create scatterplot matrix (also known as a pairplot) 
# Inputting the data, 'hue="species"' will colour the scatterplot according to the species column from the data set. I set "o" as
# all the markers, and used the colours blue, orange and green for the different species, keeping the same colours as previous histograms. 
sns.pairplot(Irisdata, hue= "species", markers=["o","o","o"], palette=["blue","orange","green"])
plt.savefig("Scatterplot Matrix") # Saved the figure and labelled it
plt.close() 
# I then closed the plot, as when I continued on to create a Heatmap it was instead added to the scatterplot matrix. Closing the plot prevented this from happening. 


################# Heatmap #################

# A heatmap is a type of chart that uses different shades of colours to represent data values. It can easily show the strong correlations between variables.

plt.figure(figsize=(10,11)) # Defining figure size
sns.heatmap(Irisdata.corr(),annot=True) # Creating heat map, establishing the data to be used, and annot will annotate the heatmap with values when True
plt.savefig ("Heatmap") # Saving figure and labelling it

