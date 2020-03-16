# Write a program that, depending on the first line of the input, reads an int, double or string.
# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
# •	If the data type is string, surround the input with "$".
# Print the result on the console.Write a program that,
# depending on the first line of the input, reads an int, double or string.
# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
# •	If the data type is string, surround the input with "$".
# Print the result on the console.
#
# Input	        Output
# int           10
# 5
#
# real          3.00
# 2
#
# string        $hello$
# hello


def int_func(input_value):
    return input_value * 2


def float_func(input_value):
    return input_value * 1.5


def string_func(input_value):
    return f'${input_value}$'


data_type = input()
value = input()

if data_type == 'int':
    print(int_func(int(value)))
elif data_type == 'real':
    print(f"{float_func(float(value)):.2f}")
elif data_type == 'string':
    print(string_func(value))
