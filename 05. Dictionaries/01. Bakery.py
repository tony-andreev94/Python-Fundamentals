# You will receive a single line containing some food(keys) and quantities(values)
# Example: bread 10 butter 4 sugar 9 jam 12
# Create a dictionary and print it on the console
# {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}

input_list = input().split(" ")
output_dict = {}

for index in range(0, len(input_list), 2):
    key = input_list[index]
    value = input_list[index + 1]
    output_dict[key] = int(value)

print(output_dict)
