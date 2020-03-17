# Write a program that reads the path to a file and subtracts the file name and its extension.
# Example:
# Input                                             Output:
# C:\Internal\training-internal\Template.pptx	    File name: Template
#                                                   File extension: pptx


def file_extractor(string):
    reversed_string = string[::-1]
    reversed_result = ""
    for char in reversed_string:
        if not char == "\\":
            reversed_result += char
        else:
            break
    result = ""
    for char in reversed_result[::-1]:
        if not char == ".":
            result += char
        else:
            break

    return result


def extension_extractor(string):
    reversed_str = string[::-1]
    reversed_result = ""
    for char in reversed_str:
        if not char == '.':
            reversed_result += char
        else:
            break

    return reversed_result[::-1]


file_path = input()
print(f"File name: {file_extractor(file_path)}")
print(f"File extension: {extension_extractor(file_path)}")

