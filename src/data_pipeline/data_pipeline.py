"""
Defines a data pipeline with the following stages:
    1) - Ingestion
    2) - Preprocessing
    3) - Write to Database
"""

import pandas as pd
from stages import data_ingestion
from stages import data_preprocessing


def ingest_data() -> pd.DataFrame:
    """Reads in data from CFD json"""
    return data_ingestion.read_json_data()


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms input data"""
    data_preprocessing.create_design_shape_config_column(df)
    data_preprocessing.create_individual_pressure_component_columns(df)
    data_preprocessing.create_individual_velocity_component_columns(df)
    data_preprocessing.create_pressure_magnitude_column(df)
    data_preprocessing.create_velocity_magnitude_column(df)
    data_preprocessing.create_lift_to_drag_ratio_column(df)
    return df


def main() -> None:
    """Calls pipeline stages (steps) in order.
    
    Stages:
        1 - Ingest (Read in) data
        2 - Transform/Preprocess data
        3 - Write data to database
    """
    df = ingest_data()
    processed_df = transform_data(df)

    print(processed_df.info())


if __name__ == "__main__":
    main()
