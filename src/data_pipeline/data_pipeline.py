"""
Defines a data pipeline with the following stages:
    1) - Ingestion
    2) - Preprocessing
    3) - Write to Database


Future Improvements:
    - Taipy Pipeline (implement)
    - Not using subprocess
"""

import os
import subprocess
import sqlite3
import pandas as pd

from stages import data_ingestion
from stages import data_preprocessing
from stages import data_write


DATABASE_PATH = "src/database/cfd_data.db"


def ingest_data() -> pd.DataFrame:
    """Reads in data from CFD json"""
    return data_ingestion.read_json_data()


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms input data"""
    data_preprocessing.create_design_shape_config_column(df)
    data_preprocessing.create_individual_pressure_component_columns(df)
    data_preprocessing.create_individual_velocity_component_columns(df)
    data_preprocessing.create_pressure_magnitude_column(df)
    data_preprocessing.create_lift_to_drag_ratio_column(df)
    data_preprocessing.convert_timestamps_to_strings(df)
    return df


def write_data_to_database(df: pd.DataFrame) -> None:
    """Populates database with data from provided
    pandas dataframe.
    
    Creates the SQLite database if it does not already exist.
    """

    if not os.path.exists(DATABASE_PATH):
        print(f"Creating {DATABASE_PATH}")
        subprocess.run(["python",
                        "src/database/create_db.py"],
                        check=True)

    conn = sqlite3.connect(DATABASE_PATH)
    data_write.populate_cfd_simulations_table(conn, df)
    conn.close()


def main() -> None:
    """Calls pipeline stages (steps) in order.
    
    Stages:
        1 - Ingest (Read in) data
        2 - Transform/Preprocess data
        3 - Write data to database
    """
    df = ingest_data()
    processed_df = transform_data(df)
    write_data_to_database(processed_df)


if __name__ == "__main__":
    main()
