# Write a program to read a list of integers and find how many odd items it holds.


def convert_to_int_list(input_list):
    int_list = []
    for x in input_list:
        if x != '-':
            int_list.append(int(x))

    return int_list


def count_odd_numbers(input_list):
    odd_counter = 0
    for x in input_list:
        if x % 2 != 0:
            odd_counter += 1

    return odd_counter


if __name__ == "__main__":
    my_list = input().split(" ")
    result = count_odd_numbers(convert_to_int_list(my_list))
    print(result)
