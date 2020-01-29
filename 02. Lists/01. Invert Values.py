# Write a program that receives a single string containing numbers separated by a single space.
# Print a list containing the opposite of each number
# Input	            Output
# 1 2 -3 -3 5	    [-1, -2, 3, 3, -5]
# -4 0 2 57 -101	[4, 0, -2, -57, 101]

input_list = [int(x) for x in input().split()]
target_list = list()
for element in input_list:
    target_list.append(element * -1)

print(target_list)
