# You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource
# (e.g. Gold, Silver, Copper, and so on) and every even – quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]

command_input = input()
result_dict = {}

while not command_input == 'stop':
    if command_input not in result_dict:
        result_dict[command_input] = int(input())
    else:
        result_dict[command_input] += int(input())
    command_input = input()

for item in result_dict.items():
    print(f"{item[0]} -> {item[1]}")
