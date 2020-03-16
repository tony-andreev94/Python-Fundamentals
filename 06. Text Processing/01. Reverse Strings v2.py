# You will be given series of strings until you receive an "end" command.
# Write a program that reverses strings and prints each pair on separate line in format "{word} = {reversed word}".


def reverse_func(string):
    return string[::-1]


def reverse_func_2(string):
    """
    Another way to reverse a string.
    :param string: the string to be reversed
    :return: returns the reversed string
    """
    return "".join(reversed(string))


result_dict = {}
# Take input
input_string = input()

while not input_string == "end":
    result_dict[input_string] = reverse_func(input_string)
    input_string = input()

for each_item in result_dict.items():
    print(f"{each_item[0]} = {each_item[1]}")
