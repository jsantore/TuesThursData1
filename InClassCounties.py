countries = []
with open("CountryData.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()
    for line in all_lines[1:]:
        data = line.strip().split("*")
        current_country ={} # make a dictionary
        current_country["name"] = data[1]
        current_country["pop2026"] = data[2]
        current_country["pop_change_percent"] = data[3]
        current_country["pop_change_num"] = data[4]
        current_country["pop_density"] = data[5]
        current_country["fertility_rate"] = data[8]
        current_country["median_age"] = data[9]
        countries.append(current_country)

while True:
    menu_text = """
[1] Find the largest population increase
[2] Find the 'largest' population decrease
[3] Find all counties with a young median population
[4] Find high population density countries
[5] Quit
    """
    print(menu_text)
    choice = input("Enter your choice:")
    if choice == "1":
        largest_so_far = countries[0]
        for current_country in countries:
            current_pop = int(current_country["pop_change_num"])
            largest_pop = int(current_country["pop_change_num"])
            if current_pop > largest_pop:
                largest_so_far = current_country
        print(f"""The largest population change  is {largest_so_far['pop_change_num']} in {largest_so_far['name']} """)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        break
    else:
        print("Please enter a valid choice")