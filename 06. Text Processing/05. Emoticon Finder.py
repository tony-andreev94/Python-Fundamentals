# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.


def find_emoji(text):
    result = ""
    for index in range(len(text)):
        if text[index] == ":":
            if index + 1 < len(text) and text[index + 1] != " ":  # check remark
                result += f"{text[index]}{text[index + 1]}" + "\n"
    return result


input_text = input()
print(find_emoji(input_text))

# Remark:
# if the condition was "OR" instead of "AND" an exception will be thrown as the second condition will be tested and if
# there is no next index (: is the last element) there will be an exception. Since "AND" requires both conditions
# to be true to return true if the first condition is false the second condition is not checked
