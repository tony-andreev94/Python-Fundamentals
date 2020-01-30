# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives a list of positive integers and checks if each integer is a palindrome or not.
# Print the results on the console
# The input will be a single string containing the numbers separated by comma and space ", "
#
# Input	                Output
# 123, 323, 421, 121	False
#                       True
#                       False
#                       True
# !!! The task is to have an input list of positive integers


def palindrome_func(input_list):
    for item in input_list:
        reversed_item = str(item)[::-1]
        if item == int(reversed_item):
            print("True")
        else:
            print("False")


my_list = [int(x) for x in input().split(", ")]
palindrome_func(my_list)
