# Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list:
# Type in a list of 4 elements - user gives all elements at once
# Give a multiplicand
# Return the multiplied items without storing them in a list


def list_multiplication(input_list, multiplicator):
    for y in input_list:
        new_element = multiplicator * y
        print(new_element, end=" ")


if __name__ == "__main__":
    data_list = list(map(int, input().split(" ")))
    multiplicand = int(input())
    list_multiplication(data_list, multiplicand)

