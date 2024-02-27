# test git
print("Hello World!")

import functions as f
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.linalg import svd 
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# Data import
wimbledon_path = "./data/tennis/Wimbledon-men-2013.csv"
women_path = "data/tennis/Wimbledon-women-2013.csv"
df2_path = "data/tennis/tennis12.csv"

tennis = pd.read_csv(wimbledon_path)
tennis.rename(columns=lambda x: x.replace(".1", "1").replace(".2","2"), inplace=True)

women_tennis = pd.read_csv(women_path)
women_tennis.rename(columns=lambda x: x.replace(".1", "1").replace(".2", "2"), inplace=True)

#Modifying dataframe such that they have only one column with players names
tennis_extended_men = pd.read_csv(df2_path, sep=',')

to_drop1 = [column for column in women_tennis.columns if "2" in column]
to_drop1.extend(['Round', 'Result', 'ST111'])
to_drop2 = [column for column in women_tennis.columns if "1" in column]
to_drop2.extend(['Round', 'Result'])

women1_int = women_tennis.drop(columns=to_drop1)
women1_int.rename(columns=lambda x: x.replace("1", ""), inplace=True)
women2_int = women_tennis.drop(columns=to_drop2)
women2_int.rename(columns=lambda x: x.replace("2", ""), inplace=True)

women_extended = pd.concat([women1_int.reset_index(drop=True), women2_int.reset_index(drop=True)], axis= 0, ignore_index = True)
women_extended.to_csv("data/tennis/women12.csv", sep=',', index=False)


tennis_extended_men.rename(columns={'Player1': 'Player'}, inplace=True)


fig0 = px.scatter(tennis, x='Player1', y='FSP1', color='FSW1', labels={'FSW1': 'First Serve Win'})
# y = First serve percentage, color = first serve won
fig0.update_layout(
    xaxis_title='Player 1',
    yaxis_title='First Serve Player 1',
    title = 'Plot 1'
)

fig1 = px.scatter(tennis, x='Player1', y='SSP1', color='FSW1', labels={'FSW1': 'First Serve Win'})
fig1.update_layout(
    xaxis_title='Player 1',
    yaxis_title='Second Serve Player 1',
    title = 'Plot 2'
)

fig2 = px.scatter(tennis, x='FSW1', y='ACE1', )

fig0.show()
fig1.show()
fig2.show()

# Check if players only appear in 1 column or both
lst_pl1, lst_pl2 = tennis['Player1'], tennis['Player2']

pl1_unique_lst = np.unique(lst_pl1)
pl2_unique_lst = np.unique(lst_pl2)

pl1_in_pl2_check = np.isin(pl1_unique_lst, pl2_unique_lst)
sum_pl1 = sum(pl1_in_pl2_check)
pl2_in_pl1_check = np.isin(pl2_unique_lst, pl1_unique_lst)
sum_pl2 = sum(pl2_in_pl1_check)
print(len(pl1_in_pl2_check))







# PCA Analysis

# Replace NaNs with 0s
tennis.replace(np.NaN, 0, inplace=True)
# Extract Features' names
cols = tennis.columns[2:]
# Extract Player 1 names
player1_names = tennis['Player1']
# Extract unique player 1 names and pair them to an integer
player1_unique = np.unique(player1_names)
players_dict = dict(zip(player1_unique, range(len(player1_unique))))

# Pair each player to an integer
y = np.array([players_dict[value] for value in player1_names])

# Convert data frame into matrix 
X = tennis[cols].values

# Compute values of N, M, and C
N = len(y)
M = len(cols)
C = len(player1_unique)

# Subtract mean from data
Y = X - np.ones((N, 1)) * X.mean(0)

# Principal Component Analysis using Singular Value Decomposition
U, S, Vh = svd(Y, full_matrices=False)

# transpose Vh to obtain what we need
V = Vh.T

# Project data  onto Principal component space
Z = Y @ V

# Indices of data we want to display

i = 0 
j = 1

fig = make_subplots()

# Iterate over each class
for c in range(C):
    # Select indices belonging to class c
    class_mask = y == c
    
    # Add a scatter trace for each class
    fig.add_trace(go.Scatter(
        x=Z[class_mask, i],
        y=Z[class_mask, j],
        mode='markers',
        marker=dict(opacity=0.7),
        name=player1_unique[c]
    ))

# Update layout
fig.update_layout(
    title="Wimbledon Men 2013: PCA",
    xaxis=dict(title=f"PC{i+1}"),
    yaxis=dict(title=f"PC{j+1}"),
    showlegend=True
)

# Show the plot
fig.show()
a = 0


y_men, men_name, Z_men_ext = f.PCA(tennis_extended_men, 'Player', (1,2), 1, title="Wimbledon 2013 Men's torunament")
y_women, women_name, Z_wom_ext = f.PCA(women_extended, 'Player', (1,2), 1, title="Wimbledon 2013 Women's tournament")