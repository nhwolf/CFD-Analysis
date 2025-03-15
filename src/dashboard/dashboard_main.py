"""
Main dashboard file to render the dashboard data
"""


import pandas as pd
from taipy.gui import Gui
import taipy.gui.builder as tgb
from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH


with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    cfd_df = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)

designs = cfd_df["design"].unique().tolist()
shapes = cfd_df["shape_id"].unique().tolist()


with tgb.Page() as data_table_page:
    tgb.text("# **Simulation Data**", mode="md")
    tgb.selector(
        value = "{designs}",
        lov = designs,
        dropdown = True,
        multiple=True,
        label = "Select Design"
    )
    tgb.selector(
        value = "{shapes}",
        lov = shapes,
        dropdown = True,
        multiple=True,
        label = "Select Shape"
    )
    tgb.html("br")
    tgb.table(data="{cfd_df}")



Gui(page=data_table_page).run(
    title="CFD Dashboard",
    dark_mode=False,
    auto_port=True)