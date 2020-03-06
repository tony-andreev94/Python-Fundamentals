# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"
#
# Input	                Output
# bread: 4                  Products in stock:
# cheese: 2                 - bread: 5
# ham: 1                    - cheese: 2
# bread: 1                  - ham: 1
# statistics	            Total Products: 3
#                           Total Quantity: 8

products_


