# test git
print("Hello World!")

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Data import
wimbledon_path = "./data/tennis/Wimbledon-men-2013.csv"
tennis = pd.read_csv(wimbledon_path)
tennis.rename(columns=lambda x: x.replace(".1", "1").replace(".2","2"), inplace=True)


fig = px.scatter(tennis, x='Player1', y='FNL1', color='Player2')
fig.update_layout(
    xaxis_title='X-axis',
    yaxis_title='Y-axis'
)

fig.show()

# Summary statistics
print(tennis[['Round ', 'Result ']].describe())
#'Round ', 'Result ', 'FNL1 ', 'FNL2 ', 'FSP1 ', 'FSW1 ', 'SSP1 ', 'SSW1 ', 'ACE1 ', 'DBF1 ', 'WNR1 ', 'UFE1 ', 'BPC1 ', 'BPW1 ', 'NPA1 ', 'NPW1 ', 'TPW1 ', 'ST11 ', 'ST21 ', 'ST31 ', 'ST41 ', 'ST51 ', 'FSP2 ', 'FSW2 ', 'SSP2 ', 'SSW2 ', 'ACE2 ', 'DBF2 ', 'WNR2 ', 'UFE2 ', 'BPC2 ', 'BPW2 ', 'NPA2 ', 'NPW2 ', 'TPW2 ', 'ST12 ', 'ST22 ', 'ST32 ', 'ST42 ', 'ST52'