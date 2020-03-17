# Write a program that receives a single string and on the first line prints all the digits,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter and one other characters.
# Alternative solution:


def divide_text(string):
    digits_result = ""
    text_result = ""
    others_result = ""
    for each_char in string:
        if each_char.isdigit():
            digits_result += each_char
        elif each_char.isalpha():
            text_result += each_char
        else:
            others_result += each_char

    return f"{digits_result}\n{text_result}\n{others_result}"


input_text = input()
print(divide_text(input_text))
