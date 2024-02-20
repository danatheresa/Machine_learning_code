# test git
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns 

# Data import
wimbledon_path = "./data/tennis/Wimbledon-men-2013.csv"
tennis = pd.read_csv(wimbledon_path)
# Summary statistics
#print(tennis[['Round ', 'Result ']].describe())
#'Round ', 'Result ', 'FNL1 ', 'FNL2 ', 'FSP1 ', 'FSW1 ', 'SSP1 ', 'SSW1 ', 'ACE1 ', 'DBF1 ', 'WNR1 ', 'UFE1 ', 'BPC1 ', 'BPW1 ', 'NPA1 ', 'NPW1 ', 'TPW1 ', 'ST11 ', 'ST21 ', 'ST31 ', 'ST41 ', 'ST51 ', 'FSP2 ', 'FSW2 ', 'SSP2 ', 'SSW2 ', 'ACE2 ', 'DBF2 ', 'WNR2 ', 'UFE2 ', 'BPC2 ', 'BPW2 ', 'NPA2 ', 'NPW2 ', 'TPW2 ', 'ST12 ', 'ST22 ', 'ST32 ', 'ST42 ', 'ST52'
#print(tennis[["ST1.1 ","ST2.1 ","ST3.1 ","ST4.1 ","ST5.1 "]])
#sns.boxplot( x=tennis["FNL.1 ", "FNL.2 "])
#tennis[["ST1.1 ","ST2.1 ","ST3.1 ","ST4.1 ","ST5.1 "]].boxplot()
#plt.show()

# For summary statistics it doesnt really matter if something was done by player one or two 
# Creating new dataframe with attributes of both players in one colummn
tennis1 = tennis.drop(columns=['Player1          ','Player2         ','Round ','Result '])