# Username

username_str = input()
command = input().split()

while not command[0] == "Sign":
    if command[0] == "Case":
        if command[1] == "lower":
            username_str = username_str.lower()
        elif command[1] == "upper":
            username_str = username_str.upper()
        print(username_str)
    elif command[0] == "Reverse":
        if 0 <= int(command[1]) < len(username_str) and 0 <= int(command[2]) < len(username_str):
            # reverse the string
            reversed_str = (username_str[int(command[1]):int(command[2]) + 1])[::-1]
            print(reversed_str)
    elif command[0] == "Cut":
        if command[1] in username_str:
            username_str = ''.join(username_str.split(command[1]))
            print(username_str)
        else:
            print(f"The word {username_str} doesn't contain {command[1]}.")
    elif command[0] == "Replace":
        username_str = username_str.replace(command[1], '*')
        print(username_str)
    elif command[0] == "Check":
        if command[1] in username_str:
            print("Valid")
        else:
            print(f"Your username must contain {command[1]}.")

    command = input().split()
