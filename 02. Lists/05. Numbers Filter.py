# You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result
# Input	        Output
# 5             [-2, 18, 998]
# 33
# 19
# -2
# 18
# 998
# even

n = int(input())
even_list = list()
odd_list = list()
positive_list = list()
negative_list = list()

for i in range(n):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

command = input()

if command == 'even':
    print(even_list)
elif command == 'odd':
    print(odd_list)
elif command == 'positive':
    print(positive_list)
else:
    print(negative_list)
