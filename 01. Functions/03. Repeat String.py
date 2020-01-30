# Write a function that receives a string and a repeat count n.
# The function should return a new string (the old one repeated n times).
#
# Input	        Output
# abc           abcabcabc
# 3


def string_repeater(string, multiplier):
    result = string * multiplier

    return result


input_str = input()
multiplicand = int(input())
print(string_repeater(input_str, multiplicand))
