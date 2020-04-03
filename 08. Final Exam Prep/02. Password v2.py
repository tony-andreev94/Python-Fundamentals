# Password
# https://judge.softuni.bg/Contests/Practice/Index/1767#1

import re

amount = int(input())
regex = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1"

for i in range(amount):
    password = input()
    result = re.match(regex, password)
    if result is not None:
        encrypted = result[2] + result[3] + result[4] + result[5]
        print(f"Password: {encrypted}")
    else:
        print("Try another password!")