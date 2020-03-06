# You will be given key-value pairs of products and quantities
# On the next line you will be given products to search for
# Check for each product, you have 2 possibilities:
# If you have it, print "We have {quantity} of {product} left"
# Otherwise, print "Sorry, we don't have {product}"

products_list = input().split(" ")
products_dict = {}

for index in range(0, len(products_list), 2):
    key = products_list[index]
    products_dict[key] = int(products_list[index + 1])

searched_products = input().split(" ")

for each_item in searched_products:
    if each_item in products_dict.keys():
        print(f"We have {products_dict[each_item]} of {each_item} left")
    else:
        print(f"Sorry, we don't have {each_item}")

