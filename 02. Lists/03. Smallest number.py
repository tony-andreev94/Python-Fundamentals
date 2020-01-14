# Write a program to read a list of integers, finds the smallest item and prints it.


def find_min_number(input_list):
    min_number = input_list[0]
    for x in input_list:
        if x < min_number:
            min_number = x

    return min_number


if __name__ == "__main__":
    my_list = [int(x) for x in input().split()]
    print(find_min_number(my_list))
