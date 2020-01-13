# Draw at the console a filled square of size n like in the example
# 4:
#
# --------
# -\/\/\/-
# -\/\/\/-
# --------


def outer_print(num):
    for i in range(1, 2 * num):
        print("-", end="")
    print("-")


def inner_print(num):
    print("-", end="")
    for i in range(1, num):
        print("\/", end="")
    print("-")


if __name__ == "__main__":
    number = int(input())
    outer_print(number)
    inner_print(number)
    inner_print(number)
    outer_print(number)
