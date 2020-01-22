# It's time to get in a Christmas mood. You have to decorate the house in time for the big event, but you have limited days to do so.
# You will receive allowed quantity for one type of decoration and days left until Christmas day to decorate the house.
# There are 4 types of decorations and each piece costs a price
# •	Ornament Set – 2$ a piece
# •	Tree Skirt – 5$ a piece
# •	Tree Garlands – 3$ a piece
# •	Tree Lights – 15$ a piece
# Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
# Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
# Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
# Every tenth day you lose 20 spirit, because your cat ruins all tree decorations and you have to rebuild the tree and buy one piece of tree skirt, garlands and lights. That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
# Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you lose additional 30 spirit.
#
# Input	            Output
# 1                 Total cost: 37
# 7	                Total spirit: 58

quantity = int(input())
days = int(input())

total_cost = 0
spirit = 0
is_tenth_day = False

for counter in range(1, days + 1):
    if is_tenth_day:
        quantity += 2
        is_tenth_day = False
    is_third_day = False
    if counter % 2 == 0:
        total_cost += quantity * 2
        spirit += 5
    if counter % 3 == 0:
        is_third_day = True
        total_cost += quantity * 5
        total_cost += quantity * 3
        spirit += 13
    if counter % 5 == 0:
        total_cost += quantity * 15
        spirit += 17
        if is_third_day:
            spirit += 30
    if counter % 10 == 0:
        total_cost += 23
        spirit -= 20
        is_tenth_day = True

print(f"Total cost: {total_cost}")
if is_tenth_day:
    print(f"Total spirit: {spirit - 30}")
else:
    print(f"Total spirit: {spirit}")
