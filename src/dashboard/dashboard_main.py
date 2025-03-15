"""
Main dashboard file to render the dashboard data
"""

import pandas as pd

from taipy.gui import Gui, State, Icon, navigate
import taipy.gui.builder as tgb

from data_utils.sqlite_interface import SQLiteInterface
from data_utils import queries
from data_utils.database_path import DATABASE_PATH
from page_utils import data_table_page_utils


with SQLiteInterface(DATABASE_PATH) as sqlite_database:
    cfd_df = sqlite_database.get_data(queries.GET_ALL_CFD_DATA)


designs = cfd_df["design"].unique().tolist()
shapes = cfd_df["shape_id"].unique().tolist()


# Initialize state variables
selected_designs = designs.copy()
selected_shapes = shapes.copy()
filtered_df = cfd_df.copy()


def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

with tgb.Page() as root_page:
    tgb.toggle(theme=True)
    tgb.menu(
        label="Menu",
        lov=[
            ("page1", Icon("images/data_table.png", "Data Table")),
        ],
        on_action=menu_option_selected,
    )

with tgb.Page() as data_table_page:
    with tgb.part(class_name="container"):
        tgb.text("# **Simulation Data**", mode="md")
    with tgb.part(class_name="container", columns="1 1"):
        with tgb.layout("1 1"):
            tgb.selector(
                value="{selected_designs}",
                lov=designs,
                on_change=lambda state: data_table_page_utils.filter_data(state, cfd_df),
                dropdown=True,
                multiple=True,
                label="Select Design",
                hover_text="Filter table by design"
            )
            tgb.selector(
                value="{selected_shapes}",
                lov=shapes,
                on_change=lambda state: data_table_page_utils.filter_data(state, cfd_df),
                dropdown=True,
                multiple=True,
                label="Select Shape",
                hover_text="Filter table by shape"
            )
    with tgb.part(class_name="container"):
        tgb.html("br")
        tgb.table(data="{filtered_df}")

def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

with tgb.Page() as root_page:
    tgb.toggle(theme=True)
    tgb.menu(
        label="Menu",
        lov=[
            ("page1", Icon("images/data_table.png", "Data Table")),
        ],
        on_action=menu_option_selected,
    )

pages = {"/": root_page, "page1": data_table_page}

if __name__ == "__main__":
    Gui(pages=pages).run(
        title="CFD Dashboard",
        use_reloader=True,
        port="auto",
        debug=True,
        watermark="",
        margin="4em",
    )
