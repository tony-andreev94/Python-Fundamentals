# Song Encryption
# https://judge.softuni.bg/Contests/Practice/Index/1759#1
# TODO simplify the solution (using functions, one function for uppercase letters and one for lowercase letters)
# if the char is something else("'" or " ") just add it to the result
import re

command = input()
regex = r"(^[A-Z][a-z' ]+):([A-Z ]+)$"

while command != "end":
    match = re.match(regex, command)
    if match is not None:
        artist = match[1]
        song = match[2]
        key = len(artist)
        encrypted_artist = ""
        encrypted_song = ""
        for char in artist[1:]:
            if char != "'" and char != " ":  # a-z : 97-122
                if ord(char) + key <= 122:
                    encrypted_artist += chr(ord(char) + key)
                else:
                    encrypted_artist += chr(96 + key - (122 - ord(char)))
            else:
                encrypted_artist += char
        if ord(artist[0]) + key > 90:
            encrypted_artist = chr(64 + key - (90 - ord((artist[0]))))
        else:
            encrypted_artist = chr(ord(artist[0]) + key) + encrypted_artist

        for char in song:
            if char != " ":  # A-Z 65-90
                if ord(char) + key <= 90:
                    encrypted_song += chr(ord(char) + key)
                else:
                    encrypted_song += chr(64 + key - (90 - ord(char)))
            else:
                encrypted_song += char

        print(f"Successful encryption: {encrypted_artist}@{encrypted_song}")
    else:
        print("Invalid input!")

    command = input()
