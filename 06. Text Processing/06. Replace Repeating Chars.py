# Write a program that reads a string from the console and replaces any sequence of the same letters
# with a single corresponding letter.


def erase_function(text):
    text_list = [each for each in text]
    for index in range(len(text_list)):
        if index + 1 < len(text_list) and text_list[index] == text_list[index + 1]:
            text_list[index] = 0
    return "".join(each for each in text_list if each != 0)


def alternative_solution(text):
    result = ""
    for index in range(len(text)):
        if index + 1 < len(text):
            if not text[index] == text[index + 1]:
                result += text[index]
        else:  # catch the last char of the string
            result += text[index]

    return result


string_input = input()
print(erase_function(string_input))
print(alternative_solution(string_input))
