
# Take input
journey_cost = float(input())
months_remaining = int(input())

# every odd month - spent 16% of collected money
# every fourth month - bonus + 25% of collected money

collected_money = 0

for each_month in range(1, months_remaining + 1):
    if each_month % 2 != 0 and each_month != 1:
        collected_money -= 0.16 * collected_money
    if each_month % 4 == 0:
        collected_money += 0.25 * collected_money
    collected_money += 0.25 * journey_cost

if collected_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {collected_money - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - collected_money:.2f}lv. more.")

