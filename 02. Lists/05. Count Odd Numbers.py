# Write a program to read a list of integers and find how many odd items it holds.


def count_odd_numbers(input_list):
    odd_counter = 0
    for x in input_list:
        # if x % 2 != 0:
        if not x % 2 == 0:
            odd_counter += 1

    return odd_counter


if __name__ == "__main__":
    my_list = [int(x) for x in input().split(" ")]
    result = count_odd_numbers(my_list)
    print(result)
