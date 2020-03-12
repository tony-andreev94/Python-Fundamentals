# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}

user_input = input()
result_dict = {}

# Remove whitespaces from the input string
# user_input.replace(" ", "")

for each_char in user_input:
    if each_char not in result_dict and not each_char == ' ':
        result_dict[each_char] = user_input.count(each_char)

for item in result_dict.items():
    print(f"{item[0]} -> {item[1]}")