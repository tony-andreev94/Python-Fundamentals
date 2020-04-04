# Activation keys
# https://judge.softuni.bg/Contests/Compete/Index/2302#0

key = input()
user_input = input()

while not user_input == "Generate":
    command = user_input.split(">>>")[0]
    if command == "Contains":
        substring = user_input.split(">>>")[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command == "Flip":
        start_index = int(user_input.split(">>>")[2])
        end_index = int(user_input.split(">>>")[3])
        if user_input.split(">>>")[1] == "Upper":
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
            print(key)
        elif user_input.split(">>>")[1] == "Lower":
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
            print(key)
    elif command == "Slice":
        start_index = int(user_input.split(">>>")[1])
        end_index = int(user_input.split(">>>")[2])
        key = key[:start_index] + key[end_index:]
        print(key)

    user_input = input()

print(f"Your activation key is: {key}")
