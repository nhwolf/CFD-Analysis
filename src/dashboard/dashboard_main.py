"""
Main dashboard file to render the dashboard data
"""

import pandas as pd

from taipy.gui import Gui, State
import taipy.gui.builder as tgb

from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH


with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    cfd_df = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)


designs = cfd_df["design"].unique().tolist()
shapes = cfd_df["shape_id"].unique().tolist()


# Initialize state variables
selected_designs = designs.copy()
selected_shapes = shapes.copy()
filtered_df = cfd_df.copy()


def filter_data(state: State):
    df = cfd_df.copy()
    if state.selected_designs:
        df = df[df["design"].isin(state.selected_designs)]
    if state.selected_shapes:  # Only apply filter if selection exists
        df = df[df["shape_id"].isin(state.selected_shapes)]
    state.filtered_df = df


with tgb.Page() as data_table_page:
    tgb.toggle(theme=True)
    tgb.text("# **Simulation Data**", mode="md")
    with tgb.part(class_name="container", columns="1 1"):
        with tgb.layout("1 1"):
            tgb.selector(
                value="{selected_designs}",
                lov=designs,
                on_change=filter_data,
                dropdown=True,
                multiple=True,
                label="Select Design",
            )
            tgb.selector(
                value="{selected_shapes}",
                lov=shapes,
                on_change=filter_data,
                dropdown=True,
                multiple=True,
                label="Select Shape",
            )
    with tgb.part(class_name="container"):
        tgb.html("br")
        tgb.table(data="{filtered_df}")

if __name__ == "__main__":
    Gui(page=data_table_page).run(
        title="CFD Dashboard",
        use_reloader=True,
        port="auto",
        debug=True,
        watermark="",
        margin="4em",
    )
