# Rage Quit
# Chochko will give you a series of strings followed by non-negative numbers, e.g. "a3";
# you need to print on the console each string repeated N times; convert the letters to uppercase beforehand.
# In the example, you need to write back "AAA".
# On the output, print first a statistic of the number of unique symbols used (the casing of letters is irrelevant,
# meaning that 'a' and 'A' are the same); the format shoud be "Unique symbols used {0}". Then, print the rage message itself.
# The strings and numbers will not be separated by anything.
# The input will always start with a string and for each string there will be a corresponding number.
# The entire input will be given on a single line; Chochko is too lazy to make your job easier.
# Input:            Output:
# a3                Unique symbols used: 1
#                   AAA
# aSd2&5s@1         Unique symbols used: 5
#                   ASDASD&&&&&S@
import time
start_time = time.time()


def find_unique_symbols(text):
    result_list = []
    for char in text:
        if not char.isdigit():
            result_list.append(char.lower())

    unique_symbols = len(set(result_list))
    return unique_symbols


def input_modifier(text):
    """
    A function that modifies the user input and makes it easier to work with.
    Example:
    :param text:    aSd2&5s@1
    :return:    ['aSd2', '&5', 's@1']
    """
    for char in text:
        if char.isdigit():
            text = text.replace(char, char + ' ')
    modified_input = text.split()
    return modified_input


def string_builder(text):
    work_list = input_modifier(text)
    result_list = []
    for each in work_list:
        result_list.append(each[:-1].upper() * int(each[-1]))

    return "".join(result_list)


message = input()
print(f"Unique symbols used: {find_unique_symbols(message)}")
print(string_builder(message))
#print("--- %s seconds ---" % (time.time() - start_time))