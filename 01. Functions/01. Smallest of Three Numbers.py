# Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.
#
# Input	    Output
# 2         2
# 5
# 3


def smallest_num_func(x, y, z):
    if x <= y and x <= z:
        return x
    elif y < x and y <= z:
        return y
    else:
        return z


first_int = int(input())
second_int = int(input())
third_int = int(input())

print(smallest_num_func(first_int, second_int, third_int))
