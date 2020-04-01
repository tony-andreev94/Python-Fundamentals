# Registration
# https://judge.softuni.bg/Contests/Practice/Index/1928#1

import re

inputs = int(input())
user_regex = r"(?<=U\$)[A-Z][a-z]{2,}(?=U\$)"
pass_regex = r"(?<=P@\$)[A-Za-z]{5,}\d+(?=P@\$)"
successful_registrations = 0

for i in range(inputs):
    registration_data = input()
    user_result = re.findall(user_regex, registration_data)
    pass_result = re.findall(pass_regex, registration_data)

    if len(user_result) > 0 and len(pass_result) > 0:
        successful_registrations += 1
        print("Registration was successful")
        print(f"Username: {''.join(user_result)}, Password: {''.join(pass_result)}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {successful_registrations}")
