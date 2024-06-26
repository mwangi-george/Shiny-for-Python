import plotly.express as px
from shiny.express import ui, render, input
from shinywidgets import render_plotly
from data_import import df


with ui.sidebar(bg="#4898a8"):

    ui.h1("Hello World")
    ui.input_slider("mass", "Body Mass", 2500, 6500, 3000)
    ui.input_select("sex", "Select Sex", choices=["Male", "Female"])


with ui.layout_columns():
    with ui.card():
        ui.card_header("Plot")

        @ render_plotly
        def plot():
            df_sub = df[(df["sex"] == input.sex()) & (
                df["body_mass_g"] >= input.mass())]

            if input.show_species():
                return px.scatter(df_sub, "bill_depth_mm", "bill_length_mm", color="species")
            else:
                return px.scatter(df_sub, "bill_depth_mm", "bill_length_mm")

        ui.input_checkbox("show_species", "Show Species", value=True)

    with ui.card():
        ui.card_header("Raw Data")

        @ render.data_frame
        def dat():
            return df[(df["sex"] == input.sex()) & (
                df["body_mass_g"] >= input.mass())]
