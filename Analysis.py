# Programming and Scripting Final Project - 2022

# This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code to investigate it.
# The programme must output a summary of each variable to a single text file, Save a histogram of each variable to png files and output a scatterplot of each pair of variables. 
# Perform any other analysis you think is appropriate. 

# Author: Jamie Tohall

import pandas as pd # To read in Iris.csv file which contains the Iris Data Set
import seaborn as sns # To use historgrams, scatterplots, and pairplots
import matplotlib.pyplot as plt # To create plots
import numpy as np #

# Read in the Iris data set as 'Irisdata'.
Irisdata = pd.read_csv("Iris.csv.txt")

