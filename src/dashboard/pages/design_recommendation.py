"""
Data Table page for the dashboard.

Future Improvments:
    - Handle the case where the user does not provide a numeric entry.
    - Provide a popup message to the user when the user does not provide a numeric entry.
"""

import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import State
from data_utils.get_data import CFD_DF


# DataFrame of average L/D ratio for each design and shape configuration
design_config_df = CFD_DF[["design", "shape_id", "L_D_ratio"]].copy()
design_config_df = design_config_df.groupby(
                                     ["design", "shape_id"],
                                     as_index=False)["L_D_ratio"].mean()


#Initialize state variables
desired_l_d_ratio = 0.0
recommended_design = None
recommended_shape = None
actual_l_d_ratio = None


def find_closest_design(df: pd.DataFrame, desired_l_d_ratio: float) -> dict:
    """Find the closest design configuration to the
    desired L/D ratio."""

    if desired_l_d_ratio<= 0:
        desired_l_d_ratio= 0
    
    closest_row = df.iloc[(df["L_D_ratio"] - desired_l_d_ratio).abs().idxmin()]
    
    return closest_row[["design", "shape_id", "L_D_ratio"]].to_dict()


def update_recommendations(state: State):
    """Updates the recommended design, shape, and L/D ratio."""
    try:
        desired_ld = float(state.desired_l_d_ratio) 
        result = find_closest_design(design_config_df, desired_ld)
        state.recommended_design = result["design"]
        state.recommended_shape = result["shape_id"]
        state.actual_l_d_ratio = round(result["L_D_ratio"], 2)
    except ValueError:
        state.recommended_design = None
        state.recommended_shape = None
        state.actual_l_d_ratio = None


# Page definition
with tgb.Page() as design_recommendation_page:

    with tgb.part(class_name="container"):
        tgb.text("# **Design Configuration Recommendation**",
                 mode="md",
                 class_name="pb1")
        
    with tgb.part(class_name="container"):
        tgb.text("#### **Enter a desired Lift to Drag ratio (L/D) below to receive a recommended design configuration**",
                 mode="md")

    with tgb.part(class_name="container", columns="1 1"):
        with tgb.layout("1 1"):

            with tgb.part(class_name="card"):

                with tgb.part(class_name="card"):
                    tgb.input(
                        label="Desired Lift to Drag Ratio (L/D):",
                        value="{desired_l_d_ratio}",
                        on_change=update_recommendations
                        )

            with tgb.part(class_name="card"):
                tgb.text("Recommended Design: **{recommended_design}**",
                         mode="md"
                       )
                tgb.text("Recommended Shape: **{recommended_shape}**",
                         mode="md"
                       )
                tgb.text("Predicted L/D Ratio: **{actual_l_d_ratio}**",
                         mode="md"
                       )

    tgb.text(value ="*Recommended configuration is the closest aircraft configuration from the CFD data, not actual results*",
             mode="md")
