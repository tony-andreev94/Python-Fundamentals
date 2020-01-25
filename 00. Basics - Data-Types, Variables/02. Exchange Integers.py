# Read two integer numbers and after that exchange their values by using some programming logic.
# Print the variable values before and after the exchange, as shown below:
#
# Input	        Output
# 5             Before:
# 10	        a = 5
#               b = 10
#               After:
#               a = 10
#               b = 5

a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

a_temp = a
a = b
b = a_temp

print("After:")
print(f"a = {a}")
print(f"b = {b}")
