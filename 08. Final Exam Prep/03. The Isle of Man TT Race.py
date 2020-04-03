# The Isle of Man TT Race
# https://judge.softuni.bg/Contests/Practice/Index/1759#2

import re

message = input()
regex = r"([#$%&*])([A-Za-z]+)\1=(\d+)!!(.+)"
decrypted = ""

while True:
    match = re.match(regex, message)
    if match is not None:
        decrypted = ""
        racer = match[2]
        length = int(match[3])
        if len(match[4]) == length:
            for char in match[4]:
                decrypted += chr(ord(char) + length)
            print(f"Coordinates found! {racer} -> {decrypted}")
            break
        else:
            print("Nothing found!")
            message = input()

    else:
        print("Nothing found!")
        message = input()