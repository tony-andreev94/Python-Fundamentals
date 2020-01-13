# Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list:
# Type in a list of 4 elements - user gives all elements at once
# Give a multiplicand
# Return the multiplied items without storing them in a list


def list_multiplication(list, multiplicator):
    for y in list:
        new_element = multiplicator * y
        print(new_element, end=" ")


if __name__ == "__main__":
    my_list = input().split(" ")
    numbers_list = []
    for x in my_list:
        numbers_list.append(int(x))

    multiplicand = int(input())
    list_multiplication(numbers_list, multiplicand)
