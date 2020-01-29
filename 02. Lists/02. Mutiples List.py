# Write a program that receives two numbers (factor and count) and creates a list with length of the given
# count and contains only elements that are multiples of the given factor
# Input	            Output
# 2                 [2, 4, 6, 8, 10]
# 5
#
# 1                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10

factor = int(input())
count = int(input())
target_list = list()
upper_boundary = factor * count + 1

for i in range(factor, upper_boundary, factor):
    if i % factor == 0:
        target_list.append(i)

print(target_list)
