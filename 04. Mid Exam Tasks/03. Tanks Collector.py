# Tanks collector

owned_tanks = input().split(", ")
commands_amount = int(input())

for i in range(commands_amount):
    command = input().split(", ")
    if command[0] == "Add":
        if command[1] in owned_tanks:
            print(f"Tank is already bought")
        else:
            print(f"Tank successfully bought")
            owned_tanks.append(command[1])
    if command[0] == "Remove":
        if command[1] in owned_tanks:
            print("Tank successfully sold")
            owned_tanks.remove(command[1])
        else:
            print("Tank not found")
    if command[0] == "Remove At":
        if int(command[1]) < len(owned_tanks):
            #remove at index
            del owned_tanks[int(command[1])]
            print("Tank successfully sold")
            # owned_tanks.remove(command[1])
        else:
            print("Index out of range")
    if command[0] == "Insert":
        if int(command[1]) >= len(owned_tanks):
            print("Index out of range")
        else:
            if command[2] not in owned_tanks:
                owned_tanks.insert(int(command[1]), command[2])
                print("Tank successfully bought")
            else:
                print("Tank is already bought")

# Printing output:
test_string = ", ".join(owned_tanks)
print(test_string)
