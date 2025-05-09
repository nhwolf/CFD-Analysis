"""
Main dashboard file to render the dashboard.
"""

from taipy.gui import Gui
from pages.home import homepage
from pages.design_comparison import design_comparison_page
from pages.design_recommendation import design_recommendation_page
from pages.data_table import data_table_page


root_md = """
<|navbar|>
<|content|>
"""


pages = {
    "/": root_md,
    "home": homepage,
    "Design-Comparison": design_comparison_page,
    "Design-Recommendation": design_recommendation_page,
    "CFD-Dataset": data_table_page
}

if __name__ == "__main__":

    Gui(pages=pages).run(
        title="Aircraft CFD Dashboard",
        dark_mode=False,
        #port="auto",
        watermark="",
        margin="2em",
    )
