
import pandas as pd
from sqlite_interface import SQLiteInterface


DATABASE_PATH = "src/database/cfd_data.db"


sql_query = """
select *
from cfd_simulations;
"""

with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    df = sqlite_database.get_data(sql_query)

df['date'] = pd.to_datetime(df['date'])
print(df.head(5))