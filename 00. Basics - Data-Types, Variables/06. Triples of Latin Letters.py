# Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:
# Input	    Output
# 3	        aaa
#           aab
#           aac
#           aba
#           abb
#           ...
#           ccc

num_input = int(input())

for first_i in range(num_input):
    for second_i in range(num_input):
        for third_i in range(num_input):
            print(chr(97 + first_i), end="")
            print(chr(97 + second_i), end="")
            print(chr(97 + third_i))
