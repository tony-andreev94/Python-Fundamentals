# Write a function that receives two characters and returns a single string with all the characters in between them
# according to the ASCII code.
#
# Input	    Output
# a         b c
# d


def chars_in_range(char_1, char_2):
    for ascii_counter in range(ord(char_1) + 1, ord(char_2)):
        print(chr(ascii_counter), end=" ")


first_char = input()        # 97 - a
second_char = input()       # 100 - d

chars_in_range(first_char, second_char)



