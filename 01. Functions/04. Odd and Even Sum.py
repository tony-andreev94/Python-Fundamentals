# You will receive a single number. You have to write a function that returns the sum of all even and all odd digits
# from that number as a single string like in the examples below.
#
# Input	                Output
#  1000435	            Odd sum = 9, Even sum = 4
#  3495892137259234	    Odd sum = 54, Even sum = 22


def odd_even_sum_func(input_str):
    odd_sum = 0
    even_sum = 0
    for each_char in input_str:
        if int(each_char) % 2 == 0:
            even_sum += int(each_char)
        else:
            odd_sum += int(each_char)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = int(input())
num_as_str = str(num)
odd_even_sum_func(num_as_str)
