# Write a program to read a list of strings, rotate it to the right and print its rotated items.
# Examples: 
# a b c d e    ->  e a b c d
# soft uni hi  ->  hi soft uni


# updated solution that is more universal making it easier to change the amount of rotated elements
def move_last_element(input_list):
    moved_elements = 1  # variable to change the amount of moved elements
    new_list = []
    for i in range(moved_elements):
        last_element = input_list.pop()
        new_list.append(last_element)
        for index in range(len(input_list)):
            new_list.append(input_list[index])
        print(*new_list)


if __name__ == "__main__":
    my_list = str(input()).split(" ")
    move_last_element(my_list)

