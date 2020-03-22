# Write a program to extract e-mail addresses from a string

import re


def extract_email(string):
    user_regex = r"(?<=\s)[a-zA-Z0-9]+[_\.\-]?[a-zA-Z0-9]+(?=@)"
    host_regex = r"(?<=@)[\-a-zA-Z]+[.][\-a-zA-Z]+[.]?[a-zA-Z]+"
    user_list = re.findall(user_regex, string)
    host_list = re.findall(host_regex, string)
    for index in range(len(user_list)):
        print(f"{user_list[index]}@{host_list[index]}")


string = input()
extract_email(string)
