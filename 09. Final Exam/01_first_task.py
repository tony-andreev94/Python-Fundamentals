#1

string_input = input()
commands = input()

while not commands == "Done":
    parts = commands.split()
    command = parts[0]
    if command == "Change":
        char = parts[1]
        new_char = parts[2]
        new_string = string_input.replace(char, new_char)
        string_input = new_string
        print(string_input)

    if command == "Includes":
        if parts[1] in string_input:
            print('True')
        else:
            print('False')

    if command == "End":
        last_symbols = len(parts[1])
        if string_input[-last_symbols:] == parts[1]:
            print('True')
        else:
            print('False')

    if command == 'Uppercase':
        new_string = string_input.upper()
        string_input = new_string
        print(string_input)

    if command == 'FindIndex':
        char = parts[1]
        index = string_input.find(char)
        print(index)

    if command == 'Cut':
        index = int(parts[1])
        length = int(parts[2])
        new_string = string_input[index:index+length]
        string_input = new_string
        print(string_input)

    commands = input()




