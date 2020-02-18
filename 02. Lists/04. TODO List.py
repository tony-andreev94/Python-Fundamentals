# You will receive a to do-notes until you get the command "End".
# The notes will be in the format: "{importance}-{value}".
# Return the list of to do-notes sorted by importance.
# The maximum importance will be 10

# Input	                        Output
# 2-Walk the dog                ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

command = input()
# we create a big enough list to fit all max 10 to do tasks,
# if we assign a task with priority 10(at the end of the list), we will move it 1 place closer to the end,
# and pop might delete it, therefore we create a list of 20 elements
# (assuming the worst case scenario, that we assign first task with lowest priority and every other task moves it back
temp_list = [0] * 20
result_list = []

while command != 'End':
    tokens = command.split('-')
    priority = int(tokens[0])
    note = tokens[1]
    temp_list.insert(priority - 1, note)
    temp_list.pop(priority)  # if we don't remove items after we add, we can break the indexes
    # if tasks with close priority are added (5th element gets 6th, if we add 4th element)
    command = input()

for each_item in temp_list:
    if not each_item == 0:
        result_list.append(each_item)

print(result_list)