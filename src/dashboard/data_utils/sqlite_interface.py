"""
SQLite3 Interface module.

Future Improvements:
    - Connection pooling
    - Multiple query/transaction support
    - sql injection prevention
    - Better (more specific) error handling
    - Data insertion/update methods (to use in the pipeline)
    - Logging
"""

import sqlite3
import pandas as pd


class SQLiteInterface:
    """
    Interface to the SQLite database.

    Intended usage example:
        with SQLiteInterface("path/to/database.db") as sqlite_database:
            dataframe = sqlite_database.get_data("SELECT * FROM my_table")
    """

    def __init__(self, database_path: str):
        """Initialize the SQLite Interface with the provided database path."""
        self.conn = None
        self.database_path = database_path

    def __enter__(self):
        """Establish a connection when entering a with block."""
        self.conn = self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection when exiting a with block."""
        if self.conn:
            self.conn.close()

    def _connect(self) -> sqlite3.Connection:
        """Establish a connection to SQLite database."""
        try:
            conn = sqlite3.connect(self.database_path)
            return conn
        except sqlite3.Error as e:
            raise Exception(f"Failed to connect to the database: {e}")
    
    def _reconnect_if_needed(self):
        """Check if connection has closed, reconnect if so"""
        if self.conn is None or not self.conn:
            self.conn = self._connect()

    def _validate_query_against_injection(self, query: str):
        """TO-DO: validate the SQL for potential risks via SQL injection."""
        pass

    def get_data(self, query: str) -> pd.DataFrame:
        """Returns a pandas dataframe containing data as defined in the provided SQL query."""
        if not self.conn:
            raise Exception("Not connected to SQLite")

        # TO-DO: add check for injection using _validate_query_against_injection

        # Ensure connection is valid
        self._reconnect_if_needed()

        try:
            df = pd.read_sql_query(query, self.conn)
            return df
        except Exception as e:
            raise Exception(f"Failed to query SQLite: {e}")
