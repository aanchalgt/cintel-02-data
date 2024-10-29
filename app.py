import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

# this package provides the palmer penguins dataset
import palmerpenguins 

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()


ui.page_opts(title="Palmer Penguins Data by AG", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")