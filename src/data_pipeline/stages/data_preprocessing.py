"""
Processes, cleans, and transforms the CFD data.
"""

import numpy as np
import pandas as pd


def create_individual_velocity_component_columns(
        df = pd.DataFrame) -> pd.DataFrame:
    """Provided a dataframe containing a velocity column
    where each row contains a dictionary of velocity components
    (x, y, z), seperates them out into seperate columns.
    
    TO-DO: add checks for components
    TO-DO: add specific error handling
    """
    # Velocity component columns
    df['velocity_x'] = df['velocity'].apply(lambda v: v['x'])
    df['velocity_y'] = df['velocity'].apply(lambda v: v['y'])
    df['velocity_z'] = df['velocity'].apply(lambda v: v['z'])

    # Drop original column
    df.drop(columns=['velocity'], inplace=True)


def create_individual_pressure_component_columns(
        df = pd.DataFrame) -> pd.DataFrame:
    """Provided a dataframe containing a pressure column
    where each row contains a dictionary of pressure components
    (front, rear, top, bottom), seperates them out into seperate columns.
    
    TO-DO: add checks for components
    TO-DO: add specific error handling
    """
    # Pressure component columns
    df['pressure_front'] = df['pressure'].apply(lambda p: p['front'])
    df['pressure_rear'] = df['pressure'].apply(lambda p: p['rear'])
    df['pressure_top'] = df['pressure'].apply(lambda p: p['top'])
    df['pressure_bottom'] = df['pressure'].apply(lambda p: p['bottom'])

    # Drop original column
    df.drop(columns=['pressure'], inplace=True)


def create_design_shape_config_column(df = pd.DataFrame) -> pd.DataFrame:
    """Creates a column for configuration, a combination
    of the design and shape.

    TO-DO: add checks for design and shape columns
    TO-DO: add specific error handling
    """
    df['design_shape_config'] = df['design'] + "_" + df['shape_id']
    return df


def create_pressure_magnitude_column(df = pd.DataFrame) -> pd.DataFrame:
    """Creates a column for pressure "magnitude",
    not really a true magnitude since pressure is a scalar quantity
    (no directional components). May or may not be useful in further analysis.
    Thought here is to get a single measure of total pressure influence.
    Simplying summing the different pressures could cancel out important effects.

    TO-DO: add checks for pressure component columns
    TO-DO: add specific error handling
    """
    df['pressure_magnitude'] = np.sqrt(
        df['pressure_front']**2 +
        df['pressure_rear']**2 +
        df['pressure_top']**2 +
        df['pressure_bottom']**2)
    return df


def create_lift_to_drag_ratio_column(df = pd.DataFrame) -> pd.DataFrame:
    """Lift to Drag Ratio (L/D): A measure of how much lift an aircraft
    generates compared to the drag it experiences.
    
    L/D = Total Lift divided by Total Drag.

    TO-DO: add checks for total lift and total drag columns
    TO-DO: add specific error handling
    """
    df['L_D_ratio'] = df['total_lift'] / df['total_drag']
    return df


def convert_timestamps_to_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts all timestamp columns in a Pandas DataFrame to string format.

    Rationale: SQLite does not directly support Pandas Timestamp objects.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        pd.DataFrame: The updated DataFrame with timestamps as strings.
    """
    #df = df.copy()
    for col in df.select_dtypes(include=['datetime64[ns]',
                                         'datetime64',
                                         'timedelta64[ns]']).columns:
        df[col] = df[col].astype(str)
    return df