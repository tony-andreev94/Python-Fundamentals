# You will receive three integer numbers.
# Write a function sum_numbers() to get the sum of the first two integers and
# subtract() function that subtracts the third integer from the result.
# Wrap the two functions in a function called add_and_subtract() which will receive the three numbers
#
# Input	    Output
# 23        19
# 6
# 10


def sum_numbers(a, b):
    result = a + b

    return result


def subtract(x, y):
    result = x - y

    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(subtract(sum_numbers(first_num, second_num), third_num))
