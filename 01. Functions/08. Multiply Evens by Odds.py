# Create a program that reads an integer number and multiplies the sum of all its even digits 
# by the sum of all its odd digits


def find_sum(num):
    even_sum_internal = 0
    odd_sum_internal = 0
    for char in str(num):
        if char != '-':
            if int(char) % 2 == 0:
                even_sum_internal += int(char)
            else:
                odd_sum_internal += int(char)

    return even_sum_internal * odd_sum_internal


if __name__ == "__main__":
    number = int(input())
    result = find_sum(number)
    print(result)
