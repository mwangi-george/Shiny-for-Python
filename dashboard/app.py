from shiny.express import ui, render, input
from pathlib import Path
import pandas as pd


file_path = Path(__file__).parent / "penguins.csv"

df = pd.read_csv(file_path)

ui.h1("Hello World")

ui.input_slider("mass", "Body Mass", 2500, 5000, 3000)
ui.input_select("sex", "Select Sex", choices=["Male", "Female", None])


@ render.data_frame
def dat():
    val = input.sex()
    print(val)
    return df[df["sex"] == val]


@ render.text
def text():
    return "I love shiny"
