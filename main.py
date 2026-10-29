from nicegui import ui

# here at the top we have several constants that we use throughupt the program
WIDTH = 1200
HEIGHT = 1000
horizontal_axis_pos = 800
# this is the list of shape strings that we will use for the first graph
shapes_list = []
second_shapes_list = []
# if we build the title label first, it will show up on the webpage above the other elements
title = ui.label("How Much More do MA tech Jobs Pay than US?")
title.style("font-size: 20px")
# we then add the interactive image for the first graph
graph = ui.interactive_image(size=(WIDTH, HEIGHT))
graph.classes("w-lg bg-stone-100")
graph2 = ui.interactive_image(size=(WIDTH, HEIGHT))
graph2.classes("w-lg bg-green-100")
# the string that describes the two axes can be added to both graphs
horizontal_axis = f"""<line x1=100 y1={horizontal_axis_pos} x2={WIDTH} y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(horizontal_axis)
vertical_axis = f"""<line x1=100 y1=0 x2=100 y2={horizontal_axis_pos} stroke='black' stroke-width=4 />"""
shapes_list.append(vertical_axis)
second_shapes_list.append(horizontal_axis)
second_shapes_list.append(vertical_axis)
for amount in range(0, 36_000, 5000):
    location = horizontal_axis_pos- amount/50
    axis_label = f'''<text x=10  y={location} fill='black'font-size=18 >
${amount} </text>'''
    shapes_list.append(axis_label)
# now open the file and process the data to create the graph
with open("MedianSalariesTech.txt", "r") as file:
    file_lines = file.readlines()
    file_lines = file_lines[1:]  # the first line is the header
    xpos = 100  # the x position of the left edge of the bar, starts at the vertical axis
    bar_color = "black"  # create a bar color before the loop so we use the same variable for all bars
    for line in file_lines:
        data = line.split("~")
        stringsalary2025 = data[3]
        us_salary_2025 = int(stringsalary2025[1:])  # slice to remove the dollar sign
        string_ma_salary2024 = data[4]
        ma_salary_2024 = int(string_ma_salary2024[1:])
        # turns out the data runs from -1050 to 31170 be careful of the first
        salary_difference = ma_salary_2024 - us_salary_2025
        # draw bars in different colors depending on the salary difference from MA to all US
        if salary_difference > 25_000:
            bar_color = "green"
        elif salary_difference > 15_000:
            bar_color = "yellow"
        elif salary_difference > 7000:
            bar_color = "red"
        elif salary_difference > 0:
            bar_color = "blue"
        else:
            bar_color = "purple"
        # the salary difference goes to 31 thousand plus, so we need to scale it down to fit the graph
        bar_height = salary_difference / 50
        # the one tech job where MA pays less than all US needs to show up on the graph
        if bar_height < 0:  # so we will need to flip the bar upside down
            bar_height = bar_height * -1
        # finally create the strings representing the bar and label and add them to the list
        bar = f"""<rect  x={xpos} y={horizontal_axis_pos-bar_height} 
        height={bar_height} width=100 fill='{bar_color}' />"""
        bar_label = f"""<text x="{xpos+40}" y="{horizontal_axis_pos-bar_height}" 
        fill='black' font-size=16 writing-mode="vertical-rl" > {data[0]} </text>"""
        shapes_list.append(bar)
        shapes_list.append(bar_label)
        xpos = xpos + 100  # update the x position for the next bar
# turn the list of strings describing what to draw into a single string
shapes_as_big_string = "\n".join(shapes_list)
graph.set_content(shapes_as_big_string)
second_shapes_string = "\n".join(second_shapes_list)
graph2.set_content(second_shapes_string)
ui.run()
