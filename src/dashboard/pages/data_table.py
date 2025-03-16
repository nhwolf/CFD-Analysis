"""
Data Table page for dashboard.
"""

import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import State, download
import pandas as pd
from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH


with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    cfd_df = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)


# Unique values for designs and shapes
designs = cfd_df["design"].unique().tolist()
shapes = cfd_df["shape_id"].unique().tolist()


# Initialize state variables
selected_designs = designs.copy()
selected_shapes = shapes.copy()
filtered_df = cfd_df.copy()
download_csv_path = None


def filter_data(state: State):
    """Filter data based on selected designs and shapes."""
    df = cfd_df.copy()

    if state.selected_designs:
        df = df[df["design"].isin(state.selected_designs)]

    if state.selected_shapes:
        df = df[df["shape_id"].isin(state.selected_shapes)]

    state.filtered_df = df


def download_csv(state: State):
    """Download the filtered DataFrame as a CSV."""
    csv_path = "filtered_data.csv"
    state.filtered_df.to_csv(csv_path, index=False)
    state.download_csv_path = csv_path
    download(state, state.download_csv_path)


# Page definition
with tgb.Page() as data_table_page:

    with tgb.part(class_name="container"):
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
                hover_text="Filter table by design"
            )
            tgb.selector(
                value="{selected_shapes}",
                lov=shapes,
                on_change=filter_data,
                dropdown=True,
                multiple=True,
                label="Select Shape",
                hover_text="Filter table by shape"
            )

    with tgb.part(class_name="container"):
        tgb.html("br")
        tgb.table(data="{filtered_df}")

    with tgb.part(class_name="container"):
        tgb.button(
            on_action=download_csv,
            label="Download dataset",
            hover_text="Download the filtered data as a CSV"
        )
