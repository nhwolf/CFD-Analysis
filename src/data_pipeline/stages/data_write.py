"""
Writes the data out to SQLite database.
"""

import sqlite3
import pandas as pd


def populate_cfd_simulations_table(conn: sqlite3.Connection, df: pd.DataFrame):
    """Writes data from provided dataframe to
    database table.
    """
    cursor = conn.cursor()

    # Prepare the data to insert (convert each row to a tuple)
    data_to_insert = [
        (
            row.simulation_id, row.shape_id, row.date,
            row.design, row.total_lift, row.total_drag, row.speed,
            row.velocity_x, row.velocity_y, row.velocity_z,
            row.pressure_front, row.pressure_rear, 
            row.pressure_top, row.pressure_bottom,
            row.design_shape_config, 
            row.pressure_magnitude, row.L_D_ratio
        )
        for row in df.itertuples(index=False)
    ]

    # executemany for batch insertion (more efficient for large data)
    cursor.executemany("""
    INSERT OR REPLACE INTO cfd_simulations (simulation_id, shape_id, date, design,
                                 total_lift, total_drag, speed,
                                 velocity_x, velocity_y, velocity_z, pressure_front,
                                 pressure_rear, pressure_top, pressure_bottom,
                                 design_shape_config, pressure_magnitude, L_D_ratio)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data_to_insert)

    conn.commit()
    print(f"Successfully inserted {len(df)} rows into the database.")
