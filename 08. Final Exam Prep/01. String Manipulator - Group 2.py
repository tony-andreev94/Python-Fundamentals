# String Manipulator - Group 2
# https://judge.softuni.bg/Contests/Practice/Index/1749#0

string = input()
command = input().split()

while command[0] != "Done":
    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        new_string = string.replace(char, replacement)
        string = new_string
        print(string)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif command[0] == "End":
        end = command[1]
        if string[-len(end):] == end:
            print("True")
        else:
            print("False")
    elif command[0] == "Uppercase":
        new_string = string.upper()
        string = new_string
        print(string)
    elif command[0] == "FindIndex":
        char = command[1]
        index = string.index(char)
        print(index)
    elif command[0] == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        new_string = string[start_index: start_index + length]
        string = new_string
        print(string)

    command = input().split()
