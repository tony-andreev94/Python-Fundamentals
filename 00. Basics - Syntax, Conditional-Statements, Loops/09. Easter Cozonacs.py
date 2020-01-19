budget = float(input())
flour_price = float(input())

# kozunak recipe:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
kozunak_price = eggs_price + flour_price + 0.25 * milk_price

eggs_counter = 0
kozunak_counter = 0

while budget > 0:
    #budget -= kozunak_price
    if budget - kozunak_price > 0:
        budget -= kozunak_price
        kozunak_counter += 1
        if kozunak_counter % 3 == 0:
            # TO_DO - check eggs
            eggs_counter += 1
        else:
            eggs_counter += 3
    else:
        break

print(f"You made {kozunak_counter} cozonacs! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
