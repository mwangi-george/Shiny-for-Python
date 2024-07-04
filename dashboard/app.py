import plotly.express as px
from shiny.express import ui, render, input
from shinywidgets import render_plotly
from data_import import df
from shiny import reactive

# context manager
with ui.sidebar():

    ui.h1("Hello World")
    ui.input_slider("mass", "Body Mass", 2500, 6500, 3000)
    ui.input_radio_buttons("sex", "Select Sex", choices=["Male", "Female"])
    ui.input_action_button("refresh_button", "Refresh", color="red")
    ui.hr()

    ui.input_text("new_label", "New Label")
    ui.input_action_button("update", "Update")


@reactive.effect()
@reactive.event(input.update)
def update_label():
    ui.update_radio_buttons("sex", label=input.new_label())
    ui.update_text("new_label", value="")


@reactive.calc
@reactive.event(input.refresh_button, ignore_none=False)
def filtered_data():
    return df[(df["sex"] == input.sex()) & (
        df["body_mass_g"] >= input.mass())]


with ui.layout_columns():
    with ui.card():
        ui.card_header("Plot")

        @ render_plotly
        def plot():
            df_sub = filtered_data()

            if input.show_species():
                return px.scatter(df_sub, "bill_depth_mm", "bill_length_mm", color="species")
            else:
                return px.scatter(df_sub, "bill_depth_mm", "bill_length_mm")

        ui.input_checkbox("show_species", "Show Species", value=True)

    with ui.card():
        ui.card_header("Raw Data")

        @ render.data_frame
        def dat():
            return filtered_data()

with ui.layout_columns():
    with ui.card():
        ui.card_header("Testing")
        ui.input_text("password", "Enter Password")

    with ui.card():
        @render.express
        def show_penguins():
            if input.password() == "1234":
                @render.data_frame
                def dat2():
                    return filtered_data()
