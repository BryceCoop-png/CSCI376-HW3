from nicegui import ui

# with ui.row().classes("mx-auto"):
#     with ui.card():
#         ui.label("Hello world! Making changes").classes("text-xl")

#     with ui.card():
#         ui.label("Hello world! Making changes")

with ui.row().classes("mx-auto"):
    with ui.card():
        input_field = ui.input(on_change = lambda e: result.set_text(e.value.lower()))
        result = ui.label()

ui.run()