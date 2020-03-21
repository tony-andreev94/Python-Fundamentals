# Write a program that reads N lines of strings and extracts the name and age of a given person.
# The name of the person will be between '@' and '|'. The person’s age will be between '#' and '*'.
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name and age print a line in the following format "{name} is {age} years old."


def find_name(string):
    name = ""
    counter = 1
    for index in range(len(string)):
        if string[index] == '@':
            while True:
                letter = string[index + counter]
                if letter != '|':
                    name += letter
                    counter += 1
                else:
                    break
    return name


def find_age(string):
    age = ''
    counter = 1
    for index in range(len(string)):
        if string[index] == '#':
            while True:
                number = string[index + counter]
                if number.isdigit():
                    age += number
                    counter += 1
                else:
                    break
    return age


number_of_lines = int(input())
people_dict = {}

for i in range(number_of_lines):
    text = input()
    people_dict[find_name(text)] = find_age(text)

for person, age in people_dict.items():
    print(f"{person} is {age} years old.")

