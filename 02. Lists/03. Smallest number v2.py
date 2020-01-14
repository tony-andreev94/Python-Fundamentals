# Write a program to read a list of integers, finds the smallest item and prints it.
# This is another solution, instead to search for the smallest number the list is sorted and the first item is printed


def list_sort_func(input_list):
    sorted_list = sorted(input_list)

    return sorted_list[0]


if __name__ == "__main__":
    my_list = [int(x) for x in input().split()]
    print(list_sort_func(my_list))
    # Alternative solution without additional functions or sorting is using the min(list) method:
    # print(min(my_list))
