# Write a program that finds all numbers in a sequence of strings.
# The output is all the numbers, extracted and printed on a single line – each separated by a single space.

import re


def find_numbers(string):
    regex = r"([\d]+)"
    result = re.finditer(regex, string, re.MULTILINE)
    return " ".join(each.group(0) for each in result)


user_input = input()
print(find_numbers(user_input))

