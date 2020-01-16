# Write a program that receives a single word from the user, reverses it and prints it
# Input	    Output
# Python	nohtyP
# banana	ananab

word = input()

for i in reversed(word):
    print(i, end="")
