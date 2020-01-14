# Read a list of integers and extract all square numbers from it and print them in descending order.
# A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.
from math import sqrt


def convert_to_int_list(input_list):
    int_list = []
    for x in input_list:
        if x != "-":
            # using abs() because negative ints break the sqrt function
            int_list.append(abs(int(x)))

    return int_list


def square_numb_func(input_list):
    sqrt_list = []
    for x in input_list:
        if sqrt(x) == int(sqrt(x)):
            sqrt_list.append(x)

    list.sort(sqrt_list, reverse=True)

    return sqrt_list


def print_function(input_list):
    for x in input_list:
        print(x, end=" ")


if __name__ == "__main__":
    my_list = input().split(" ")
    print_function(square_numb_func(convert_to_int_list(my_list)))
