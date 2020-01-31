# Write a function that calculates the total price of an order and prints it on the console.
# The function should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.
#
# Input	            Output
# water             5.00
# 5
# coffee            3.00
# 2


def order_func(item, amount):
    total_price = 0
    if item == 'coffee':
        total_price = 1.5 * amount
    elif item == 'water':
        total_price = 1 * amount
    elif item == 'coke':
        total_price = 1.4 * amount
    elif item == 'snacks':
        total_price = 2 * amount

    return total_price


order_item = input()
item_amount = int(input())
print(f"{order_func(order_item, item_amount):.2f}")
