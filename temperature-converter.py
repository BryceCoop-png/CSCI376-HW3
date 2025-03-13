from nicegui import ui

ui.colors(
      primary='#1976d2',
      secondary='#26a69a',
      accent='#9c27b0',
      positive='#21ba45',
      negative='#c10015',
      info='#31ccec',
      warning='#f2c037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: prints the converted temperature
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: prints an error message

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 border rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Set element border (padding) to be fixed at 6
        # shadow-xl: Set element shadow to be xl
        # mx-auto: set element x to be auto
        # mt-10: set element y to be fixed at 10
        # rounded-xl: set element bevel to be fixed at xl
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: set element text size to be fixed at 2xl
        # font-bold: set element text to be bolded
        # text-accent: set element text color to accent
        # mb-4: set element margin bottom to be fixed at 4
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: set element width to be full screen
        # border: set element to have solid line border
        # rounded: set element to have bevel
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 text-xl")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: set element text to be white
        # py-2: set element height to be fixed at 2
        # px-4: set element width to be fixed at 4
        result_label = ui.label("").classes("text-lg font-bold mt-4 border px-2")

    with ui.card().classes("w-100 mx-auto mt-10 border rounded-xl"):
        ui.label("Thermometer").classes("text-xl")
        slider = ui.slider(min=-100, max=120, value=0)
        n = ui.number().bind_value_from(slider, 'value')
        cel = n * 9/5 + 32
        ui.label().bind_text_from(slider, 'value')
        result_label = ui.label("Cel")
ui.run()