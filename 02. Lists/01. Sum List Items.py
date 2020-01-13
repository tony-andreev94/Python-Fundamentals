# Write a program, which reads a list of integers, calculates its sum and prints it.
# The input consists of a number n (the number of items) + n integers, each as a separate line.



def sum_of_list_items(list):
    list_sum = 0
    for x in my_list:
        list_sum = list_sum + x

    return list_sum


if __name__ == "__main__":
    number_of_items = int(input())
    my_list = []
    for i in range(0, number_of_items):
        list_item = int(input())
        my_list.append(list_item)
    result = sum_of_list_items(my_list)
    print(result)
