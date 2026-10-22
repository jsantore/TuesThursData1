from nicegui import ui
WIDTH=1000
HEIGHT=1000
horizontal_axis_pos = 800
graph = ui.interactive_image(size=(WIDTH, HEIGHT))
graph.classes("w-lg bg-stone-100")
horizontal_axis= f"""<line x1=100 y1={horizontal_axis_pos}> x2={WIDTH} y2={horizontal_axis_pos}</line>"""

ui.run()