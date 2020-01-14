# Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list:
# Type in a list of 4 elements - user gives all elements at once
# Give a multiplicand
# Return the multiplied items without storing them in a list


def multiply_func(list_element, multiplicand):
    return list_element * multiplicand


if __name__ == "__main__":
    my_list = list(map(int, input().split(" ")))
    # Alternative solution for reading input as list of integers:
    # my_list = [int(x) for x in input().split(" ")]
    multiply_value = int(input())
    result = [multiply_func(x, multiply_value) for x in my_list]
    # print(*result) is the python way to print the list items separated by space, without storing them in a list
    print(*result)
    # however if we want to separate the elements with another symbol and not space, we should use join:
    # print(".".join(map(str, result)))
    # join works only with strings, so we map our int elements back to str)
