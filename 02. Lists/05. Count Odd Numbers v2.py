# Write a program to read a list of integers and find how many odd items it holds.

int_list = [int(x) for x in input().split(" ")]
odd_num_list = [num for num in int_list if not num % 2 == 0]
print(len(odd_num_list))

# Alternative way for a single line solution:
# print(len([num for num in list(map(int, input().split(" "))) if num % 2 == 1]))
