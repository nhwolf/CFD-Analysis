"""
This module is used to load data from the
database and store it in a pandas DataFrame.
"""

from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH


# Load CFD data
with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    CFD_DF = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)
