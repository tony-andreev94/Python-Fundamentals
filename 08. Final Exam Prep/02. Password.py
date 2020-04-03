# Password
# https://judge.softuni.bg/Contests/Practice/Index/1767#1

import re

amount = int(input())

# REGEX
first_part_r = r"\A.+(?=>)"
last_part_r = r"(?<=\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^><]{3}<).+(?=$)"
four_groups_r = r"(?<=>)\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^><]{3}(?=<)"  # matches all 4 groups between > <
digit_group = r"(?<=>)\d{3}(?=|)"  # matches the digits group
lowercase_group = r"(?<=>\d{3}\|)[a-z]{3}(?=\|)"  # matches the lowercase letters group
uppercase_group = r"(?<=>\d{3}\|[a-z]{3}\|)[A-Z]{3}(?=\|)"  # matches the uppercase letters group
symbol_group = r"(?<=>\d{3}\|[a-z]{3}\|[A-Z]{3}\|)[^<>]{3}(?=<)"  # matches the symbols group


for i in range(amount):
    password = input()
    first_part = "".join(re.findall(first_part_r, password))
    last_part = "".join(re.findall(last_part_r, password))
    four_groups = re.findall(four_groups_r, password)
    if first_part == last_part and first_part != "" and len(four_groups) == 1:
        # password is valid, do encryption
        digits = re.findall(digit_group, password)
        lower_letters = re.findall(lowercase_group, password)
        upper_letters = re.findall(uppercase_group, password)
        symbols = re.findall(symbol_group, password)
        encrypted = "".join(digits) + "".join(lower_letters) + "".join(upper_letters) + "".join(symbols)
        print(f"Password: {encrypted}")
    else:
        print("Try another password!")
