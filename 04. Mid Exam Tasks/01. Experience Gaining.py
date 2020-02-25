# Experience Gaining

needed_exp = float(input())
battles_available = int(input())
current_exp = 0
battle_counter = 0
enough_exp = True

while current_exp < needed_exp:
    battle_exp = float(input())
    battle_counter += 1
    if battle_counter % 3 == 0:
        current_exp += (1.15 * battle_exp)
    elif battle_counter % 5 == 0:
        current_exp += (0.9 * battle_exp)
    else:
        current_exp += battle_exp

    if battle_counter == battles_available and needed_exp > current_exp:
        print(f"Player was not able to collect the needed experience, {needed_exp - current_exp:.2f} more needed.")
        enough_exp = False
        break

if enough_exp:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
