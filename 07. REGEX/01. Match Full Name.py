# First, write a regular expression to match a valid full name, according to these conditions:
# •	A valid full name has the following characteristics:
#   o	It consists of two words.
#   o	Each word starts with a capital letter.
#   o	After the first letter, it only contains lowercase letters afterwards.
#   o	Each of the two words should be at least two letters long.
#   o	The two words are separated by a single space.
import re


def find_names(string):
    regex = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
    result = re.findall(regex, string)
    return result


user_input = input()
print(*find_names(user_input))
