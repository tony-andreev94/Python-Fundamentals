# Write a program to read a list of integers, finds the smallest item and print it.

from math import inf


def find_smallest_number(input_list):
    comparison_value = inf
    for x in input_list:
        if x < comparison_value:
            comparison_value = x

    return comparison_value


def convert_to_int(input_list):
    list_of_numbers = []
    for x in input_list:
        list_of_numbers.append(int(x))

    return list_of_numbers


if __name__ == "__main__":
    my_list = input().split(" ")
    result = convert_to_int(my_list)
    printed_result = find_smallest_number(result)
    print(printed_result)
