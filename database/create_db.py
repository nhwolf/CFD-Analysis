"""
Creates a SQLite database with a table to store
CFD simulation data.
"""

import os
import sqlite3

def create_database(database_path: str) -> sqlite3.Connection:
    """
    Creates SQLite database
    """
    conn: sqlite3.Connection = sqlite3.connect(database_path)
    return conn


def create_table(conn: sqlite3.Connection) -> None:
    """Creates cfd_simulations table in provided
    SQLite database.
    """
    cursor: sqlite3.Cursor = conn.cursor()

    # Create table with the specified columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cfd_simulations (
        simulation_id TEXT PRIMARY KEY,
        shape_id TEXT NOT NULL,
        date TEXT NOT NULL,
        design TEXT NOT NULL,
        total_lift REAL NOT NULL,
        total_drag REAL NOT NULL,
        speed REAL NOT NULL,
        velocity_x REAL NOT NULL,
        velocity_y REAL NOT NULL,
        velocity_z REAL NOT NULL,
        pressure_front REAL NOT NULL,
        pressure_rear REAL NOT NULL,
        pressure_top REAL NOT NULL,
        pressure_bottom REAL NOT NULL,
        design_shape_config TEXT NOT NULL,
        velocity_magnitude REAL NOT NULL,
        pressure_magnitude REAL NOT NULL,
        L_D_ratio REAL NOT NULL
    );
    """)

    conn.commit()


def main() -> None:
    """Creates database and table."""
    
    database_name = "cfd_data.db"

    script_dir = os.path.dirname(os.path.abspath(__file__))

    database_path = os.path.join(script_dir, database_name)

    if os.path.exists(database_path):
        print(f"{database_name} already exists")
    else:
        conn = create_database(database_path)
        create_table(conn)
        conn.close()
        print(f"{database_name} created")

if __name__ == "__main__":
    main()
