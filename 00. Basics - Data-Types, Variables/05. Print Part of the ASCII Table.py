# Write a program that prints part of the ASCII table of characters on the console.
# On the first line of input you will receive the char index you should start with
# and on the second line - the index of the last character you should print.
# Input	    Output
# 60        < = > ? @ A
# 65
#
# 69        E F G H I J K L M N O
# 79

first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    print(chr(i), end=" ")
