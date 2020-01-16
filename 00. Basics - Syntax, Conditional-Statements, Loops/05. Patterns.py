# Write a program to create the following pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# You will receive a number that represents the highest number of stars.


def first_part_print(number):
    for i in range(1, number + 1):
        for j in range(0, i):
            print('*', end="")
        print()


def second_part_print(number):
    for i in range(number - 1, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()


if __name__ == "__main__":
    max_stars = int(input())
    first_part_print(max_stars)
    second_part_print(max_stars)



