# Write a program, which finds all integer and floating-point numbers in a string.
import re


def find_number(string):
    regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
    result = re.finditer(regex, string)
    for match in result:
        print(match.group(0), end=" ")


user_input = input()
find_number(user_input)
