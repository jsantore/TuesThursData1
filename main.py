from nicegui import ui
WIDTH=1200
HEIGHT=1000
horizontal_axis_pos = 800
shapes_list = []
title = ui.label("How Much More do MA tech Jobs Pay than US?")
title.style("font-size: 20px")
graph = ui.interactive_image(size=(WIDTH, HEIGHT))
graph.classes("w-lg bg-stone-100")
horizontal_axis= f"""<line x1=100 y1={horizontal_axis_pos} x2={WIDTH} y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(horizontal_axis)
vertical_axis = f"""<line x1=100 y1=0 x2=100 y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(vertical_axis)
with open("MedianSalariesTech.txt", "r") as file:
    file_lines = file.readlines()
    file_lines = file_lines[1:]
    xpos =100
    bar_color = 'black'
    for line in file_lines:
        data = line.split('~')
        stringsalary2025 =data[3]
        us_salary_2025=int(stringsalary2025[1:])
        string_ma_salary2024= data[4]
        ma_salary_2024=int(string_ma_salary2024[1:])
        #turns out the data runs from -1050 to 31170 be careful of the first
        salary_difference = ma_salary_2024 - us_salary_2025
        if salary_difference > 25_000:
            bar_color = 'green'
        elif salary_difference > 15_000:
            bar_color = 'yellow'
        elif salary_difference > 7000:
            bar_color = 'red'
        elif salary_difference >0:
            bar_color = 'blue'
        else:
            bar_color = "purple"
        bar_height = salary_difference/50
        if bar_height < 0:
            bar_height=bar_height*-1
        bar = f'''<rect  x={xpos} y={horizontal_axis_pos-bar_height} 
        height={bar_height} width=100 fill='{bar_color}' />'''
        bar_label = f'''<text x="{xpos+40}" y="{horizontal_axis_pos-bar_height}" 
        fill='black' font-size=16 writing-mode="vertical-rl" > {data[0]} </text>
'''

        shapes_list.append(bar)
        shapes_list.append(bar_label)
        xpos = xpos+100
shapes_as_big_string = "\n".join(shapes_list)
graph.set_content(shapes_as_big_string)
ui.run()