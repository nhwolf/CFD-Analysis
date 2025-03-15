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

'''
def filter_by_design(state):
    state.data = cfd_df[cfd_df["design"] == state.selected_design]
    state.chart_date = (
        state.data
    )'
'''



with tgb.Page() as data_table_page:
    with tgb.part(class_name="container"):
        tgb.text("# **Simulation Data**", mode="md")
        tgb.selector(
            value="{designs}",
            lov=designs,
            #on_change=filter_by_design,
            dropdown=True,
            multiple=True,
            label="Select Design"
        )
        tgb.selector(
            value="{shapes}",
            lov=shapes,
            #on_change=filter_by_shape,
            dropdown=True,
            multiple=True,
           label="Select Shape"
        )
    with tgb.part(class_name="container"):
        tgb.html("br")
        tgb.table(data="{cfd_df}")


if __name__ == "__main__":
    Gui(page=data_table_page).run(
        title="CFD Dashboard",
        use_reloader=True,
        port="auto",
        debug=True,
        watermark="", # removes watermark
        margin="4em"
    )
