# import re

email = input()
command = input().split()

while command[0] != "Complete":
    if command[0] == "Make":
        if command[1] == "Upper":
            new_email = email.upper()
            email = new_email
            print(email)
        elif command[1] == "Lower":
            new_email = email.lower()
            email = new_email
            print(email)
    elif command[0] == 'GetDomain':
        count = int(command[1])
        print(email[-count:])
    elif command[0] == "GetUsername":
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            result = ""
            for each in email:
                if each != '@':
                    result += each
                else:
                    break
            print(result)
    elif command[0] == "Replace":
        char = command[1]
        new_email = email.replace(char, '-')
        email = new_email
        print(email)
    elif command[0] == "Encrypt":
        for each in email:
            print(ord(each), end=" ")

    command = input().split()
