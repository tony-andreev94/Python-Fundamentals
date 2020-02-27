# Man O War

pirate_ship = input().split(">")
battle_ship = input().split(">")
max_hp = int(input())
command = input().split(" ")
needs_repair = 0
stalemate = True
pirate_ship_sum = 0
battle_ship_sum = 0

while command[0] != "Retire":
    if command[0] == "Fire":
        if 0 <= int(command[1]) < len(battle_ship):
            battle_ship[int(command[1])] = int(battle_ship[int(command[1])]) - int(command[2])
            if int(battle_ship[int(command[1])]) <= 0:
                print(f"You won! The enemy ship has sunken.")
                stalemate = False
                break

    elif command[0] == "Defend":
        if 0 <= int(command[1]) < len(pirate_ship) and 0 <= int(command[2]) < len(pirate_ship):
            for index in range(int(command[1]), int(command[2]) + 1):
                if int(pirate_ship[index]) - int(command[3]) <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
            break

    elif command[0] == "Repair":
        if 0 < int(command[1]) < len(pirate_ship):
            pirate_ship[int(command[1])] += command[2]
            if int(pirate_ship[int(command[1])]) > max_hp:
                pirate_ship[int(command[1])] = str(max_hp)

    elif command[0] == "Status":
        print(pirate_ship)
        for each_section in pirate_ship:
            if int(each_section) < 0.2 * max_hp:
                needs_repair += 1

        print(f"{needs_repair} sections need repair.")

    command = input().split(" ")

if stalemate:
    for each_item in pirate_ship:
        pirate_ship_sum += int(each_item)

    for each_item in battle_ship:
        battle_ship_sum += int(each_item)

    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {battle_ship_sum}")




