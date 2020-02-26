# Weaponsmith

# Take input
parts = input().split("|")
command = input().split()

even_indexes = list()
odd_indexes = list()

# Logic
while not command[0] == "Done":
    if command[0] == "Move":
        if command[1] == "Left":
            if 0 < int(command[2]) < len(parts):
                parts[int(command[2])], parts[int(command[2]) - 1] = parts[int(command[2]) - 1], parts[int(command[2])]
        elif command[1] == "Right":
            if 0 <= int(command[2]) < len(parts) - 1:
                parts[int(command[2])], parts[int(command[2]) + 1] = parts[int(command[2]) + 1], parts[int(command[2])]

    elif command[0] == "Check":
        if command[1] == "Even":
            for index in range(len(parts)):
                if index % 2 == 0:
                    even_indexes.append(parts[int(index)])
            print(" ".join(even_indexes))
            even_indexes = []   # the list is emptied, otherwise we will have duplicated elements on the second check
        if command[1] == "Odd":
            for index in range(len(parts)):
                if index % 2 != 0:
                    odd_indexes.append(parts[int(index)])
            print(" ".join(odd_indexes))
            odd_indexes = []   # the list is emptied, otherwise we will have duplicated elements on the second check

    command = input().split()

# Print output
weapon = "".join(parts)
print(f"You crafted {weapon}!")
