fires_collection = input().split("#")
amount_water = int(input())


efforts = 0
cells = []


for current_fire in fires_collection:
    fire = current_fire.split(" = ")
    type_of_fire = fire[0]
    value_of_cell = int(fire[1])
    if amount_water >= value_of_cell:
        if type_of_fire == "High":
            if 81 <= value_of_cell <= 125:
                amount_water -= value_of_cell
                efforts += value_of_cell * 0.25
                cells.append(value_of_cell)
        elif type_of_fire == "Medium":
            if 51 <= value_of_cell <= 80:
                amount_water -= value_of_cell
                efforts += value_of_cell * 0.25
                cells.append(value_of_cell)
        elif type_of_fire == "Low":
            if 1 <= value_of_cell <= 50:
                amount_water -= value_of_cell
                efforts += value_of_cell * 0.25
                cells.append(value_of_cell)

print("Cells:")
for cell in cells:
    print(f"- {cell}", end="\n")

print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {sum(cells)}")