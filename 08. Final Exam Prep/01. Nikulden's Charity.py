# Nikulden charity
# https://judge.softuni.bg/Contests/Practice/Index/1929#0

string = input()
command = input().split()

while command[0] != "Finish":
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        new_string = string.replace(current_char, new_char)
        string = new_string
        print(string)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string) and start_index <= end_index:
            new_string = string[:start_index] + string[end_index + 1:]
            string = new_string
            print(string)
        else:
            print("Invalid indexes!")
    elif command[0] == "Make":
        if command[1] == "Upper":
            new_string = string.upper()
            string = new_string
            print(string)
        else:
            new_string = string.lower()
            string = new_string
            print(string)
    elif command[0] == "Check":
        sub_string = command[1]
        if sub_string in string:
            print(f"Message contains {sub_string}")
        else:
            print(f"Message doesn't contain {sub_string}")
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string) and start_index <= end_index:
            new_string = string[start_index:end_index + 1]
            result = 0
            for each in new_string:
                result += ord(each)
            print(result)
        else:
            print("Invalid indexes!")

    command = input().split()

