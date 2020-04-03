# Email Validator
# https://judge.softuni.bg/Contests/Practice/Index/1928#0

import re

email = input()
command = input().split(" ")

while not command[0] == "Complete":
    if command[0] == "Make":
        if command[1] == "Upper":
            email = email.upper()
            print(email)
        else:
            email = email.lower()
            print(email)

    elif command[0] == "GetDomain":
        count = command[1]
        regex = ".{" + count + "}$"
        last_el = re.findall(regex, email)
        print("".join(last_el))

    elif command[0] == "GetUsername":
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            regex = r".+(?=@)"
            username = re.findall(regex, email)
            print("".join(username))
    elif command[0] == "Replace":
        char = command[1]
        email = email.replace(char, '-')
        print(email)
    elif command[0] == "Encrypt":
        print(" ".join([str(ord(each)) for each in email]))

    command = input().split(" ")

