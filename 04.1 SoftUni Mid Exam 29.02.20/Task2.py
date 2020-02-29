# Shopping list program:
#
# Input
# You will receive an initial list with groceries separated by "!".
# After that you will be receiving 4 types of commands, until you receive "Go Shopping!"
# •	Urgent {item} - add the item at the start of the list.  If the item already exists, skip this command.
# •	Unnecessary {item} - remove the item with the given name, only if it exists in the list. Otherwise skip this command.
# •	Correct {oldItem} {newItem} – if the item with the given old name exists, change its name with the new one. If it doesn't exist, skip this command.
# •	Rearrange {item} - if the grocery exists in the list, remove it from its current position and add it at the end of the list.
# Constraints
# •	There won`t be any duplicate items in the initial list
#
# Output
# Print the list with all the groceries, joined by ", ".
# •	"{firstGrocery}, {secondGrocery}, …{nthGrocery}"

# Input
shopping_list = input().split("!")
command = input().split(" ")

# Main loop
while command[0] != "Go":
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])

    elif command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])

    elif command[0] == "Correct":
        if command[1] in shopping_list:
            index = shopping_list.index(command[1])
            shopping_list[index] = command[2]

    elif command[0] == "Rearrange":
        if command[1] in shopping_list:
            shopping_list.append(command[1])
            shopping_list.remove(command[1])

    command = input().split(" ")

# Output
print(", ".join(shopping_list))
