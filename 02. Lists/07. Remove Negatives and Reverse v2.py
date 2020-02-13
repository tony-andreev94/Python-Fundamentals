# #Write a program to read a list of integers, remove the negative integers from the list
# and print the resulted list in reversed order.


# numbers_list = [int(x) for x in input().split()]
numbers_list = list(map(int, input().split()))

positive_numbers_list = list(filter(lambda num: num >= 0, numbers_list))

if len(numbers_list) == 0:
    print('empty')
    exit(0)
else:
    print(*positive_numbers_list[::-1])
