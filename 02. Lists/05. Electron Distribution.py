# Write a program that receives a list of numbers
# (string containing integers separated by ", ") and prints lists with the numbers them into lists of 10's.
#
# Input                                 Output
# 8, 12, 38, 3, 17, 19, 25, 35, 50      Group of 10's: [8, 3]
#                                       Group of 20's: [12, 17, 19]
#                                       Group of 30's: [25]
#                                       Group of 40's: [38, 35]
#                                       Group of 50's: [50]

# 1, 3, 3, 4, 34, 35, 25, 21, 33        Group of 10's: [1, 3, 3, 4]
#                                       Group of 20's: []
#                                       Group of 30's: [25, 21]
#                                       Group of 40's: [34, 35, 33]

# TODO: Easier solution with dictionaries
# >>> groups = {}
# >>> for i in range(1, 21):
# ...     groups['l' + str(i)] = []
# ...
# >>> groups
# {'l18': [], 'l19': [], 'l20': [], 'l14': [], 'l15': [], 'l16': [], 'l17': [], 'l10': [], 'l11': [], 'l12': [], 'l13': [], 'l6': [], 'l7': [], 'l4': [], 'l5': [], 'l2': [], 'l3': [], 'l1': [], 'l8': [], 'l9': []}
# >>>

input_list = list(int(x) for x in input().split(', '))
max_number = max(input_list)
groups_list = list()  # used inside the print

# Generate groups list:
for i in range(10, max_number + 10, 10):
    groups_list.append(i)

# Generate n amount of lists
generated_lists = list([] for each_item in groups_list)

# Assign elements to lists
for element in input_list:
    index = (element - 1) // 10

    generated_lists[index].append(element)

# Print the result
temp_index = 10
for each_list in generated_lists:
    print(f"Group of {temp_index}'s: {each_list}")
    temp_index += 10
