# Create a program that checks if inputs are valid and decrypt it. On the first line you will receive a number that indicates how many inputs you will receive on the next lines.
# You will read lines with a boss name and title and you should check if they are valid, considering the following rules:
# 	Boss - the name should be in upper case letters, should be minimum four letters long and should be surrounded by "|"
# 	Title - contains exactly 2 words and they contain only alphabetical letters and 1 whitespace between them. The title should be surrounded by "#"
# 	The name and title should be split by a single ":"
# Example for a valid input:  |GEORGI|:#Lead architect#
# If the input is valid. Print in the following format:
# "{boss name}, The {title}
# >> Strength: {length of the name}
# >> Armour: {length of the title}"
# If the input is invalid, print "Access denied!"

import re


def find_name(string):
    regex = r"\|[A-Z]+\|"
    name = re.findall(regex, string)
    result = "".join(name).strip('|')
    if len(result) >= 4:
        return result
    else:
        return None


def find_title(string):
    regex = r"(?<=\|\:\#)[A-Za-z]+[ ][A-Za-z]+(?=#)"
    title = re.findall(regex, string)
    print(title)
    if len(title) > 0:
        return "".join(title)
    else:
        return None


def return_results(string):
    name = find_name(string)
    title = find_title(string)
    if name is not None and title is not None:
        return f"{name}, The {title}\n>> Strength: {len(name)}\n>> Armour: {len(title)}"
    else:
        return "Access denied!"


lines_of_input = int(input())

for i in range(lines_of_input):
    user_input = input()
    print(return_results(user_input))
