# Write a function that receives an integer number and returns if this number is perfect or NOT.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
#
# Input	        Output 	                        Comments
# 6	            We have a perfect number!	    1 + 2 + 3
# 28	        We have a perfect number!	    1 + 2 + 4 + 7 + 14
# 1236498	    It's not so perfect.


def perfect_num(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    if divisor_sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


if __name__ == "__main__":
    num_input = int(input())
    perfect_num(num_input)
