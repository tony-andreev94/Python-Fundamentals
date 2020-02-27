# Treasure hunt

initial_loot = input().split("|")
command = input().split(" ")
stolen_items = []
length_sum = 0

while command[0] != "Yohoho!":
    if command[0] == "Loot":
        for counter in range(1, len(command)):
            if command[counter] not in initial_loot:
                initial_loot.insert(0, command[counter])

    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(initial_loot):
            initial_loot.append(initial_loot[int(command[1])])
            initial_loot.pop(int(command[1]))

    elif command[0] == "Steal":
        if int(command[1]) <= len(initial_loot):
            for i in range(int(command[1])):
                stolen_items.append(initial_loot[-1])
                initial_loot.pop(-1)
            print(", ".join(reversed(stolen_items)))
        else:
            stolen_items = initial_loot
            print(", ".join(stolen_items))
            initial_loot = []

    command = input().split(" ")
    stolen_items = []

for each_item in initial_loot:
    length_sum += len(each_item)


if len(initial_loot) > 0:
    average_gain = length_sum / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")




