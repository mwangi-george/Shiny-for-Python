from shiny.express import ui, render
from pathlib import Path
import pandas as pd


file_path = Path(__file__).parent // "penguins.csv"

df = pd.read_csv(file_path)

ui.h1("Hello World")


@render.data_frame
def dat():
    return df


@render.text
def text():
    return "I love shiny"
