"""
Module to provide functions for common plotting/figure generation.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_scatter(
            df: pd.DataFrame, 
            x_col: str, 
            y_col: str, 
            color_col: str = None, 
            size_col: str = None, 
            title: str = "Scatter Plot"
            ) -> go.Figure:
    """
    Creates a scatter plot using Plotly Express.

    Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        x_col (str): The column name for the x-axis.
        y_col (str): The column name for the y-axis.
        color_col (Optional[str]): The column name for color grouping (default: None).
        size_col (Optional[str]): The column name for point sizes (default: None).
        title (str): The title of the plot (default: "Scatter Plot").

    Returns:
        go.Figure: The scatter plot figure.
    """
    fig = px.scatter(
        df, 
        x=x_col, 
        y=y_col, 
        color=color_col, 
        size=size_col,
        title=title, 
        template="plotly_white",
    )
    fig.update_traces(marker=dict(opacity=0.7,
                                  line=dict(width=1,
                                            color="DarkSlateGrey")))
    fig.update_layout(xaxis_title=x_col, yaxis_title=y_col)

    return fig


def plot_facet_grid(df: pd.DataFrame,
                    x_col: str,
                    y_col: str,
                    facet_col: str,
                    color_col: str
                    ) -> go.Figure:
    """
    Creates a facet grid for each design with L/D ratio vs.
    speed using Plotly Express.

    Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        x_col (str): The column name for the x-axis (Speed).
        y_col (str): The column name for the y-axis (L/D Ratio).
        facet_col (str): The column name to facet the plot (Design).
        color_col (str): The column name for color grouping (Shape ID).

    Returns:
        plotly.graph_objects.Figure: The facet grid scatter plot figure.
    """
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        facet_col=facet_col,
        color_continuous_scale='Set1',  # Choose the color palette
        opacity=0.7
    )

    facet_titles = fig.layout['annotations']
    for title in facet_titles:
        title['text'] = title['text'].split('=')[1]

    fig.update_traces(marker=dict(opacity=0.7,
                                  line=dict(width=1,
                                            color="DarkSlateGrey")))
    fig.update_layout(
        xaxis_title="Speed",
        yaxis_title="Lift-to-Drag Ratio (L/D)",
        legend_title="Shape",
        legend=dict(title="Shape", x=0.02, y=1.2, orientation="h"),
        template="plotly_white"
    )

    return fig

