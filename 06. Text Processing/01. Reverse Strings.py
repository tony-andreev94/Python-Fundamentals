# You will be given series of strings until you receive an "end" command.
# Write a program that reverses strings and prints each pair on separate line in format "{word} = {reversed word}".

string = input()

while not string == "end":
    reverse_string = string[::-1]
    print(f"{string} = {reverse_string}")
    string = input()
