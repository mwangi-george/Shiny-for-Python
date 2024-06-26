from shiny.express import ui, render, input
from pathlib import Path
import pandas as pd


file_path = Path(__file__).parent / "penguins.csv"

df = pd.read_csv(file_path)

ui.h1("Hello World")

ui.input_slider("mass", "Body Mass", 2000, 3000, 400)


@render.data_frame
def dat():
    val = input.mass()
    print(val)
    return df[df["body_mass_g"] < val]


@render.text
def text():
    return "I love shiny"
