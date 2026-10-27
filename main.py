from nicegui import ui
WIDTH=1200
HEIGHT=1000
horizontal_axis_pos = 800
shapes_list = []
graph = ui.interactive_image(size=(WIDTH, HEIGHT))
graph.classes("w-lg bg-stone-100")
horizontal_axis= f"""<line x1=100 y1={horizontal_axis_pos} x2={WIDTH} y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(horizontal_axis)
vertical_axis = f"""<line x1=100 y1=0 x2=100 y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(vertical_axis)
with open("MedianSalariesTech.txt", "r") as file:
    file_lines = file.readlines()
    file_lines = file_lines[1:]
    for line in file_lines:
        data = line.split('~')
        stringsalary2025 =data[3]
        us_salary_2025=int(stringsalary2025[1:])
        string_ma_salary2024= data[4]
        ma_salary_2024=int(string_ma_salary2024[1:])
        #the difference ranges from -$1050 t0 $31170
shapes_as_big_string = "\n".join(shapes_list)
graph.set_content(shapes_as_big_string)
ui.run()