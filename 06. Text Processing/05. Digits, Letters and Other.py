# Write a program that receives a single string and on the first line prints all the digits,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter and one other characters.


def extract_digits(string):
    result = ""
    for each_char in string:  # 48 - 57
        if 48 <= ord(each_char) <= 57:
            result += each_char

    return result


def extract_letters(string):
    result = ""
    for each_char in string:  # 97 - 122; 65 - 90
        if 65 <= ord(each_char) <= 90 or 97 <= ord(each_char) <= 122:
            result += each_char

    return result


def extract_special_symbols(string):
    result = ""
    for each_char in string:
        if not 48 <= ord(each_char) <= 57 and not 65 <= ord(each_char) <= 90 and not 97 <= ord(each_char) <= 122:
            result += each_char

    return result


input_text = input()
print(extract_digits(input_text))
print(extract_letters(input_text))
print(extract_special_symbols(input_text))
