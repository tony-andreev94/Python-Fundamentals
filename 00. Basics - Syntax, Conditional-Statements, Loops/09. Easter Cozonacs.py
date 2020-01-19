# Create a program that calculates how much cozonacs you can make with the budget you have.
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# Here is the recipe for one cozonac:
#
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
#
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1l milk is 25% more than price for 1 kg flour.
# Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
# Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
# •	For every cozonac that you make, you will receive 3 colored eggs.
# •	For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received
# the usual 3 colored eggs for your cozonac. The count of eggs you will lose is calculated when you
# subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)
# In the end, print the cozonacs you made, the eggs you have gathered and the money you have left,
# formatted to the 2nd decimal place, in the following format:
# "You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."


budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
kozunak_price = eggs_price + flour_price + 0.25 * milk_price
eggs_counter = 0
kozunak_counter = 0

while budget > 0:
    if budget - kozunak_price > 0:
        budget -= kozunak_price
        kozunak_counter += 1
        if kozunak_counter % 3 == 0:
            eggs_counter += 3
            eggs_counter = eggs_counter - (kozunak_counter - 2)
        else:
            eggs_counter += 3
    else:
        break

print(f"You made {kozunak_counter} cozonacs! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
