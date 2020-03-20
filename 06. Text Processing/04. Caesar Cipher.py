# Write a program that returns an encrypted version of the same text.
# Encrypt the text by shifting each character with three positions forward.
# For example A would be replaced by D, B would become E, and so on. Print the encrypted text.


def cipher_func(string):
    result = ""
    for each_char in string:
        new_char = chr(ord(each_char) + 3)
        result += new_char
    return result


def comprehension_solution(string):
    return "".join([chr(ord(char) + 3) for char in string])


message = input()
print(cipher_func(message))
print(comprehension_solution(message))
