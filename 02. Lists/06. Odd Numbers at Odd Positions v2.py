# This is 6th problem from the SoftUni's List exercise, but instead to return the odd element and it's index,
# it just counts them


def convert_to_int_list(input_list):
    int_list = []
    for x in input_list:
        if x != '-':
            int_list.append(int(x))

    return int_list


def take_ints_on_odd_indexes(input_list):
    odd_index_list = []
    for index in range(len(input_list)):
        if index % 2 != 0:
            odd_index_list.append(input_list[index])

    return odd_index_list


def count_odd_numbers(input_list):
    odd_counter = 0
    for x in input_list:
        if x % 2 != 0:
            odd_counter += 1

    return odd_counter


if __name__ == "__main__":
    my_list = input().split(" ")
    result = count_odd_numbers(take_ints_on_odd_indexes(convert_to_int_list(my_list)))
    #result = count_odd_numbers(convert_to_int_list(my_list))
    print(result)
