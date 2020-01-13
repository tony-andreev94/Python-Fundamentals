# Write a program to read a list of integers and find how many odd numbers at odd positions the list holds.
# If there are no numbers, which match this criterion, do not print anything
# Input:
# 2 3 5 2 7 9 -1 -7
#
# Output:
# Index 1 -> 3
# Index 5 -> 9
# Index 7 -> -7


def convert_list_to_int(input_list):
    int_list = []
    for x in input_list:
        if x != '-':
            int_list.append(int(x))

    return int_list


def odd_nums_odd_positions(input_list):
    for index in range(len(input_list)):
        if index % 2 != 0:
            if input_list[index] % 2 != 0:
                print(f"Index {index} -> {input_list[index]}")


if __name__ == "__main__":
    my_list = input().split(" ")
    odd_nums_odd_positions(convert_list_to_int(my_list))
