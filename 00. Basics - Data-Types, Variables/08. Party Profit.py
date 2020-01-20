# As a young adventurer, you travel with your party around the world, seeking for gold and glory.
# But you need to split the profit among your companions.
# You will receive a party size. After that you receive the days of the adventure.
#
# Every day, you are earning 50 coins, but you also spent 2 coin per companion for food.
# Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion.
# But if you have a motivational party the same day, you spent additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
# but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You have to calculate how much coins gets each companion at the end of the adventure.
# Input	    Output
# 3         3 companions received 90 coins each.
# 5
#

party_size = int(input())
adventure_days = int(input())
days_spent = 0
coins = 0

while True:
    is_motivational_day = False
    days_spent += 1
    if days_spent % 10 == 0:
        party_size -= 2
    if days_spent % 15 == 0:
        party_size += 5
    coins += 50
    coins -= 2 * party_size
    if days_spent % 3 == 0:
        # motivational day -> - 3 coins per member
        coins -= 3 * party_size
        is_motivational_day = True
    if days_spent % 5 == 0:
        # slaying boss +20 coins per member, if is_motivational_day = True -> -2 additional coins per member
        coins += 20 * party_size
        if is_motivational_day:
            coins -= 2 * party_size

    if days_spent == adventure_days:
        break

print(f"{party_size} companions received {int(coins / party_size)} coins each.")
