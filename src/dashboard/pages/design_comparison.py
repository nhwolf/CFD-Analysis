"""
Design comparison page for the dashboard.
"""

import taipy.gui.builder as tgb
from data_utils.get_data import CFD_DF
from plotting_utils.plotting_utils import plot_scatter, plot_facet_grid, plot_line_over_time


# Design Datasets
design_a_df = CFD_DF[CFD_DF["design"] == "Design_A"]
design_b_df = CFD_DF[CFD_DF["design"] == "Design_B"]


# Plots
design_a_scatter_plot = plot_scatter(
    df=design_a_df,
    x_col="total_drag",
    y_col="total_lift",
    color_col="shape_id",
    title="Design A"
    )

design_b_scatter_plot = plot_scatter(
    df=design_b_df,
    x_col="total_drag",
    y_col="total_lift",
    color_col="shape_id",
    title="Design B"
    )

design_facet_plot = plot_facet_grid(
    df=CFD_DF,
    x_col="speed",
    y_col="L_D_ratio",
    facet_col="design",
    color_col="shape_id"
    )

lift_to_drag_ratio_over_time_plot = plot_line_over_time(
    df=CFD_DF,
    date_col="date",
    y_col="L_D_ratio",
    group_col="design_shape_config"
    )


# Page definition
with tgb.Page() as design_comparison_page:

    with tgb.part(class_name="container"):
        tgb.text("# **Design Comparison**", mode="md")

    with tgb.part(class_name="container"):
        tgb.text("## **Lift versus Drag**", mode="md")

    with tgb.part(class_name="container", columns="1 1"):
        with tgb.layout("1 1" , class_name="pb1"):
            tgb.chart(
                figure="{design_a_scatter_plot}"
                )
            tgb.chart(
                figure="{design_b_scatter_plot}"
            )
    with tgb.part(class_name="container"):
        tgb.text("## **Lift to Drag Ratio**", mode="md")

    with tgb.part(class_name="container"):
        with tgb.layout("1" , class_name="pb1"):
            tgb.chart(
                figure="{design_facet_plot}"
                )

    with tgb.part(class_name="container"):
        tgb.text("## **Lift to Drag Ratio Over Time**", mode="md")

    with tgb.part(class_name="container"):
        tgb.chart(
            figure="{lift_to_drag_ratio_over_time_plot}"
            )
