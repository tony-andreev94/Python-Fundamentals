# Given a string, you have to print a string in which each character (case-sensitive) is repeated once.
# Input	            Output
# Hello World	    HHeelllloo  WWoorrlldd
# 1234!	            11223344!!

user_input = input()

for x in user_input:
    print(x, end="")
    print(x, end="")
