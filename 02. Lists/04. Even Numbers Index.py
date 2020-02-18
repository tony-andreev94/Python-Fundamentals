# Write a program that reads a single string with numbers separated by comma and space ", "
# Print the indices of all even numbers

numbers_list = input().split(', ')
result_list = list()

for each_item in numbers_list:
    if int(each_item) % 2 == 0:
        result_list.append(numbers_list.index(each_item))

print(result_list)

# Alternative solution
numbers = list(map(lambda x: int(x), input().split(', ')))
even_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
