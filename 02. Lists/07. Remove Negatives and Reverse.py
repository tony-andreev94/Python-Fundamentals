# #Write a program to read a list of integers, remove the negative integers from the list
# and print the resulted list in reversed order


def convert_to_int_list(input_list):
    int_list = []
    for x in input_list:
        if x != '-':
            int_list.append(int(x))
    return int_list


def remove_negatives_and_reverse(input_list):
    result_list = []
    counter = 0
    for x in input_list:
        if x >= 0:
            result_list.append(x)
            counter += 1

    if counter > 0:
        for i in reversed(result_list):
            print(i, end=" ")
    else:
        print("empty")


if __name__ == "__main__":
    my_list = input().split(" ")
    remove_negatives_and_reverse(convert_to_int_list(my_list))
