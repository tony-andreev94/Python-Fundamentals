# Write a program that receives a single string and on the first line prints all the digits,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter and one other characters.
# Alternative solution:


def extract_digits(string):
    return "".join(each_char for each_char in string if each_char.isdigit())


def extract_letters(string):
    return "".join(each_char for each_char in string if each_char.isalpha())


def extract_special_symbols(string):
    return "".join(each_char for each_char in string if not each_char.isalnum())


def result_func():
    return f"{extract_digits(input_text)}\n{extract_letters(input_text)}\n{extract_special_symbols(input_text)}"


input_text = input()
print(result_func())
