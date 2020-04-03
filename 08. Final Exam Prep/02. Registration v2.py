# Registration
# https://judge.softuni.bg/Contests/Practice/Index/1928#1

import re

amount = int(input())
regex = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[0-9]+)P@\$"
successful = 0

for i in range(amount):
    registration = input()
    result = re.match(regex, registration)
    if result is not None:
        successful += 1
        print("Registration was successful")
        print(f"Username: {result[1]}, Password: {result[2]}")
    else:
        print("Invalid username or password")
    pass

print(f"Successful registrations: {successful}")