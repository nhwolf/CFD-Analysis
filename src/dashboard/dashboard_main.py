"""
Main dashboard file to render the dashboard.
"""

from taipy.gui import Gui
from pages.home import homepage
from pages.data_table import data_table_page

root_md = """
<|navbar|>
<|content|>
"""

pages = {
    "/": root_md,
    "home": homepage,
    "CFD-Dataset": data_table_page
}

if __name__ == "__main__":

    Gui(pages=pages).run(
        title="CFD Dashboard",
        use_reloader=True,
        port="auto",
        debug=True,
        watermark="",
        margin="2em",
    )
