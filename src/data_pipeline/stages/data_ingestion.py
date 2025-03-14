"""
Reads data in from the provided CFD json source.
"""

import pandas as pd


SOURCE_CFD_DATA = "data_source/data.json"


def read_json_data() -> pd.DataFrame:
    """Reads the provided CFD json file as
    a pandas dataframe.
    """
    return pd.read_json(SOURCE_CFD_DATA)
