# String Manipulator - Group 1
# https://judge.softuni.bg/Contests/Practice/Index/1748#0

string = input()
command = input().split()
word = command[0]

while word != "End":
    if word == "Translate":
        char = command[1]
        replacement = command[2]
        new_string = string.replace(char, replacement)
        string = new_string
        print(string)
    elif word == "Includes":
        sub_string = command[1]
        if sub_string in string:
            print("True")
        else:
            print("False")
    elif word == "Start":
        sub_string = command[1]
        if string[:len(sub_string)] == sub_string:  # check if it is -1
            print("True")
        else:
            print("False")
    elif word == "Lowercase":
        new_string = string.lower()
        string = new_string
        print(string)
    elif word == "FindIndex":
        char = command[1]
        index = string.rindex(char)
        print(index)
    elif word == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        part_one = string[:start_index]
        part_two = string[start_index + count:]
        string = part_one + part_two
        print(string)

    command = input().split()
    word = command[0]
