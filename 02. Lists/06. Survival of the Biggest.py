# Write a program that receives a list of integer numbers and a number n.
# The number n represents the amount of numbers to remove from the list. You should remove the smallest ones
#
# Input	                Output
# 10 9 8 7 6 5          [10, 9, 8]
# 3

my_list = [int(x) for x in input().split()]
n = int(input())

for i in range(n):
    to_remove = min(my_list)
    my_list.remove(to_remove)

print(my_list)