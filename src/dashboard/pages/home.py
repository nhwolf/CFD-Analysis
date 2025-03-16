"""
Home page for dashboard.
"""

import pandas as pd
import taipy.gui.builder as tgb
from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH


with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    cfd_df = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)


# Data Source Information
num_simulations = cfd_df["simulation_id"].nunique()
unique_design_count = cfd_df["design"].nunique()
unique_shape_count = cfd_df["shape_id"].nunique()
unique_design_shape_combinations = cfd_df["design_shape_config"].nunique()
min_simulation_date = pd.to_datetime(cfd_df["date"]).min().date()
max_simulation_date = pd.to_datetime(cfd_df["date"]).max().date()


# Page definition
with tgb.Page() as homepage:
    tgb.text(value ="# Computational Fluid Dynamics Data Analysis",
             mode="md")

    tgb.toggle(theme=True) # Light/Dark mode toggle

    with tgb.part(class_name="container", columns="1 1 1"):
        with tgb.layout("1 1 1", class_name="pb1"):

            with tgb.part(class_name="card"):
                tgb.text("## Number of Simulations: {num_simulations}",
                         mode="md",
                         class_name="h4 text-center p1",
                         )

            with tgb.part(class_name="card"):
                tgb.text("## Simulation Start Date: {min_simulation_date}",
                         mode="md",
                         class_name="h4 text-center p1",
                         )

            with tgb.part(class_name="card"):
                tgb.text("## Simulation End Date: {max_simulation_date}",
                          mode="md",
                          class_name="h4 text-center p1"
                         )

    with tgb.part(class_name="container"):
        with tgb.layout("1 1 1", class_name="pb1"):

            with tgb.part(class_name="card"):
                tgb.text("## Aircraft Designs: {unique_design_count}",
                         mode="md",
                         class_name="h4 text-center p2",
                         )

            with tgb.part(class_name="card"):
                tgb.text("## Aircraft Shapes: {unique_shape_count}",
                         mode="md",
                         class_name="h4 text-center p2",
                         )

            with tgb.part(class_name="card"):
                tgb.text("## Design/Shape Configurations:"
                        " {unique_design_shape_combinations}",
                          mode="md",
                          class_name="h4 text-center p1",
                         )

    tgb.text(value ="*CFD data comes from a made up aircraft with genereated data and may not represent reality*",
             mode="md")
