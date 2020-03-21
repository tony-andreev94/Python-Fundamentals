# Write a program that prints a sum of all characters between two given characters (their ascii code).
# On the first line you will get a character. On the second line you get another character.
# On the last line you get a random string. Find all the characters between the two given and print their ascii sum.
# Example:
# Input	                Output
# .                     363
# @
# dsg12gr5653feee5
#
# ?                     262
# E
# @ABCEF


def find_sum(first, second, string):
    total_sum = 0
    for char in string:
        if ord(first) < ord(char) < ord(second):
            total_sum += ord(char)
    return total_sum


first_char = input()
second_char = input()
input_string = input()
print(find_sum(first_char, second_char, input_string))
