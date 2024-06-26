import pandas as pd
from shiny.express import ui, render, input
from pathlib import Path
from shinywidgets import render_plotly
import plotly.express as px


file_path = Path(__file__).parent / "penguins.csv"

df = pd.read_csv(file_path)

with ui.sidebar(bg="#4898a8"):

    ui.h1("Hello World")


ui.input_slider("mass", "Body Mass", 2500, 6500, 3000)
ui.input_select("sex", "Select Sex", choices=["Male", "Female", None])


@ render_plotly
def plot():
    df_sub = df[(df["sex"] == input.sex()) & (
        df["body_mass_g"] >= input.mass())]
    return px.scatter(df_sub, "bill_depth_mm", "bill_length_mm", color="species", facet_col="island")


@ render.data_frame
def dat():
    return df[(df["sex"] == input.sex()) & (
        df["body_mass_g"] >= input.mass())]
