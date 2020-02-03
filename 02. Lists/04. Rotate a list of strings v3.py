# Write a program to read a list of strings, rotate it to the right and print its rotated items.
# Examples:
# a b c d e    ->  e a b c d
# soft uni hi  ->  hi soft uni


def rotating_func(input_list):
    last_element = input_list.pop()
    input_list.insert(0, last_element)
    print(*input_list)


if __name__ == "__main__":
    my_list = input().split(" ")
    rotating_func(my_list)
