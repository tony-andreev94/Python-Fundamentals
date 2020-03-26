# Write a program to extract e-mail addresses from a string

import re


def extract_email(string):
    result = ""
    regex = r"(?<=\s)[a-zA-Z0-9]+[_\.\-]?[a-zA-Z0-9]+[@][\-a-zA-Z]+[.][\-a-zA-Z]+[.]?[a-zA-Z]+\b"
    results_list = re.findall(regex, string)
    for email in results_list:
        result += email + '\n'
    return result


string = input()
print(extract_email(string))
