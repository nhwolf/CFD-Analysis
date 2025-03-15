"""
This module contains utility functions for the data table page.
"""
import pandas as pd
from taipy.gui import State

def filter_by_design(state: State, df: pd.DataFrame):
    if state.selected_designs:
        df = df[df["design"].isin(state.selected_designs)]
    return df

def filter_by_shape(state: State, df: pd.DataFrame):
    if state.selected_shapes:
        df = df[df["shape_id"].isin(state.selected_shapes)]
    return df

def filter_data(state: State, cfd_df: pd.DataFrame):
    df = cfd_df.copy()
    df = filter_by_design(state, df)
    df = filter_by_shape(state, df)
    state.filtered_df = df
