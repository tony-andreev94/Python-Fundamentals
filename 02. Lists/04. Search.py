# You will receive a number n and a word. On the next n lines you will be given some strings.
# You have to add them in a list and print them. After that you have to filter out only the strings
# that include the given word and also print that list.
# Input	                        Output
# 3                             ['I study at SoftUni', 'I walk to work', 'I learn Python at SoftUni']
# SoftUni                       ['I study at SoftUni', 'I learn Python at SoftUni']
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni

n = int(input())
target_word = input()
whole_list = list()
target_list = list()

for i in range(n):
    input_string = input()
    whole_list.append(input_string)
    if target_word in input_string:
        target_list.append(input_string)

print(whole_list)
print(target_list)
