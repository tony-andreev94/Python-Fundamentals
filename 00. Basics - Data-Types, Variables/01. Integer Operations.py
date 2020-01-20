# Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and
# multiply the result by the fourth number.
# Print the result.
# Input	    Output
# 10        30
# 20
# 3
# 3

first_num = int(input())
second_num = int(input())
third_num = int(input())
forth_num = int(input())

print(f"{int((first_num + second_num) / third_num) * forth_num:.0f}")


