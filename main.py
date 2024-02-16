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