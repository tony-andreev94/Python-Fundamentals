# You will receive how many wagons the train has
# Until you receive "End", you get some of the commands:
#   add {people} -> adds the people in the last wagon
#   insert {index} {people} -> adds the people at the given wagon
#   leave {index} {people} -> removes the people from the wagon

# Input:
# 3
# add 20
# insert 0 15
# leave 0 5
# End
#
# Output:
# [10, 0, 20]

train_length = int(input())
wagons = [0] * train_length
command = ''
# command = input()

while command != 'End':
    # Alternative solution with comments
    command = input()   # no input here
    command_parts = command.split(" ")
    if command_parts[0] == 'End':
        break
    elif command_parts[0] == 'add':
        wagons[train_length - 1] += int(command_parts[1])
    elif command_parts[0] == 'insert':
        wagons[int(command_parts[1])] += int(command_parts[2])
    elif command_parts[0] == 'leave':
        wagons[int(command_parts[1])] -= int(command_parts[2])
    # command = input()

print(wagons)
