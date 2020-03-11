# Write a program that keeps information about products and their prices.
# Each product has a name, a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity
# and if its price is different, replace the price as well.
# You will receive products' names, prices and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# When you do receive the command "buy", print the items with their names and total price of all the products with that name.


# TODO rework task as the solution is bad
def multiply_func(input_list):
    result = 1
    for each in input_list:
        result *= each

    return result


command = input().split(" ") # list
products_dict = {}

while not command[0] == "buy":
    if command[0] not in products_dict.keys():
        products_dict[command[0]] = [float(command[1]), int(command[2])]

    else:
        temp_list = products_dict[command[0]]
        quantity = temp_list[1]
        products_dict[command[0]] = [float(command[1]), int(quantity + int(command[2]))]

    command = input().split(" ")

# Print results
for each_item in products_dict.items():
    print(f"{each_item[0]} -> {multiply_func(each_item[1]):.2f}")
