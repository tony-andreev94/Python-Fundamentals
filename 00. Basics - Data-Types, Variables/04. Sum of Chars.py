# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive letters from the Latin alphabet
# Print the total sum in the following format:
# The sum equals: {total_sum}
# Input	        Output
# 5             The sum equals: 399
# A
# b
# C
# d
# E

number_of_chars = int(input())
total_sum = 0

for i in range(number_of_chars):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")
