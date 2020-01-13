# Write a program to read a list of strings, rotate it to the right and print its rotated items.
# Examples: 
# a b c d e    ->  e a b c d
# soft uni hi  ->  hi soft uni


def move_last_element(input_list):
    new_list = []
    new_list.extend(input_list[-1:])
    new_list.extend(input_list[:-1])
    for x in new_list:
        print(x, end=" ")


if __name__ == "__main__":
    my_list = str(input()).split(" ")
    move_last_element(my_list)

