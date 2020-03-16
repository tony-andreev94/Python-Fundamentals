# On the first line you will receive a string. On the second line you will receive a second string.
# Write a program that removes all of the occurrences of the first string in the second until there is no match.
# At the end print the remaining string.


def trim_function(string, trim_part):
    while trim_part in string:
        new_string = string.replace(trim_part, "")
        string = new_string

    return string


to_trim = input()
input_string = input()
print(trim_function(input_string, to_trim))
