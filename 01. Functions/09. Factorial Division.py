# Write a function that receives two integer numbers. Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

# Input	    Output
# 5         60.00
# 2


def factorial_func(x, y):
    x_sum = 1
    y_sum = 1

    for i in range(x, 1, -1):
        x_sum *= i

    for j in range(y, 1, -1):
        y_sum *= j

    # Divide the two sums and print
    print(f"{x_sum / y_sum:.2f}")


if __name__ == "__main__":
    first_num = int(input())
    second_num = int(input())
    factorial_func(first_num, second_num)
