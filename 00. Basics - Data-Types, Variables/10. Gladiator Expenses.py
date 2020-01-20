# As a gladiator, Petar has to repair his broken equipment when he loses a fight.
# His equipment consists of helmet, sword, shield and armor. You will receive the Petar`s lost fights count.
#
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.
#
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
repair_cost = 0
broken_shield_counter = 0

for lost_game in range(1, lost_fights + 1):
    broken_helmet = False
    if lost_game % 2 == 0:
        repair_cost += helmet_price
        broken_helmet = True
    if lost_game % 3 == 0:
        repair_cost += sword_price
        if broken_helmet:
            repair_cost += shield_price
            broken_shield_counter += 1
    if broken_shield_counter != 0:
        if broken_shield_counter % 2 == 0:
            repair_cost += armor_price
            broken_shield_counter = 0

print(f"Gladiator expenses: {repair_cost:.2f} aureus")
