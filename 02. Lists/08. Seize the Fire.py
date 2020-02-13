# Create a program that calculates the water that is needed to put out a "fire cell",
# based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
# Afterwards you will receive the amount of water you have for putting out the fires.
# There is a range of fire for each of the fire types, and if a cell’s value is below or exceeds it,
# it is invalid and you don’t need to put it out.
#
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
#
# If a cell is valid, you have to put it out by reducing the water with its value.
# Putting out fire also takes effort and you need to calculate it. Its value is equal to 25% of the cell’s value.
# In the end you will have to print the total effort. Keep putting out cells until you run out of water.
# If you don’t have enough water to put out a given cell – skip it and try the next one. In the end,
# print the cells you have put out in the following format:
#
# "Cells:
#  - {cell1}
#  - {cell2}
#  - {cell3}
# ……
#  - {cellN}"
# "Effort: {effort}"
# In the end, print the total fire you have put out from all of the cells in the following format:
# "Total Fire: {totalFire}"

fire_level = input().split("#")
total_water = int(input())

valid_cells_list = []
total_effort = 0
total_fire = 0

for each_element in fire_level:
    # TODO Check for a smarter way to get the digits without making a list consisting of one element
    digit_list = [int(digit) for digit in each_element.split() if digit.isdigit()]
    digit_value = digit_list[0]
    if (81 <= digit_value <= 125 and "High" in each_element) or (
            51 <= digit_value <= 80 and "Medium" in each_element) or (
            1 <= digit_value <= 50 and "Low" in each_element):
        if total_water - digit_value >= 0:
            total_water -= digit_value
            valid_cells_list.append(digit_value)
            cell_effort = 0.25 * digit_value
            total_effort += cell_effort

print("Cells:")
for item in valid_cells_list:
    print(f" - {item}")
    total_fire += item

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

