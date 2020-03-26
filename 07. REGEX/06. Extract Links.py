# Write a program that extracts links from a given text.

import re


def extract_link(string):
    regex = r"w{3}[.][A-Za-z0-9-]+[.][a-z]+[.a-z]+"
    link = re.findall(regex, string)
    if len(link) > 0:
        return "".join(link)


user_input = input()
while user_input:
    if extract_link(user_input) is not None:
        print(extract_link(user_input))
    user_input = input()
