"""
Home page for dashboard.
"""

import taipy.gui.builder as tgb

# Page definition
with tgb.Page() as homepage:
    tgb.text(value = "## Computational Fluid Dynamics Data Analysis", 
             mode = "md")
    tgb.toggle(theme=True) # Light/Dark mode toggle
