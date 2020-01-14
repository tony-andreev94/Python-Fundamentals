# Write a program to read a list of strings, rotate it to the right and print its rotated items.
# Examples:
# a b c d e    ->  e a b c d
# soft uni hi  ->  hi soft uni


def rotate_func(input_list):
    print(input_list[-1], end=" ")
    print(*input_list[:-1])


if __name__ == "__main__":
    my_list = input().split(" ")
    rotate_func(my_list)
