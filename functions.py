import numpy as np
import pandas as pd
from scipy.linalg import svd 
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def plot_pca_scatter(Z, y, name_unique, i, j, title):
    """
    Plot PCA scatter plot.

    Parameters:
    - Z: numpy array, PCA transformed data
    - y: numpy array, labels
    - name_unique: list, unique class names
    - i, j: int, indices for PC components
    - title: str, plot title

    Returns:
    (in the following order)
    - y
    - name_wunique
    - Z 
    """

    C = len(name_unique)  # Number of classes

    # Initialize subplot
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
            name=name_unique[c]
        ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis=dict(title=f"PC{i+1}"),
        yaxis=dict(title=f"PC{j+1}"),
        showlegend=True
    )

    # Show the plot
    fig.show()



def PCA(df: pd.DataFrame,
        names_col: str,
        components: tuple,
        plot_switch: bool,
        title: str
        ):

    # Replace NaNs with 0s
    df.replace(np.NaN, 0, inplace=True)

    # Extract Features' names
    cols = df.columns[2:]

    # Extract Player 1 names
    name = df[names_col]

    # Extract unique names and pair them to an integer
    name_unique = np.unique(name)
    name_dict = dict(zip(name_unique, range(len(name_unique))))

    # Pair each player to an integer
    y = np.array([name_dict[value] for value in name])

    # Convert Data frame into a matrix
    X = df[cols].values

    # Compute N, M and C
    N = len(y)
    M = len(cols)
    C = len(name_unique)

    # Subtract mean from data
    Y = X - np.ones((N, 1)) * X.mean(0)

    # PCA using singular value decomposition
    U, S, Vh = svd(Y, full_matrices=False)

    # transpose Vh to obtain what we need
    V = Vh.T

    # Project data  onto Principal component space
    Z = Y @ V

    if plot_switch:
        # Indices of data we want to display
        i, j = components

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
                name=name_unique[c]
            ))

        # Update layout
        fig.update_layout(
            title=title,
            xaxis=dict(title=f"PC{i+1}"),
            yaxis=dict(title=f"PC{j+1}"),
            showlegend=True
        )

        # Show the plot
        fig.show()

    return y, name_unique, Z
