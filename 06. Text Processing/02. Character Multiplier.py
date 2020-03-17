# Create a program that receives two strings on a single lines seperated by space and prints the sum of
# their character codes multiplied (multiply str1[0] with str2[0] and add to the total sum).
# Then continue with the next two characters. If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.
# TODO - new solution, this one is stupid and there is off by one issue


def char_multiplier(first_s, second_s):
    result = 0
    index = 0
    if len(first_s) == len(second_s):
        for each_char in first_s:
            result += (ord(each_char) * ord(second_s[index]))
            index += 1
    else:
        if len(first_s) < len(second_s):
            smaller_len = len(first_s)
            smaller = 1
        else:
            smaller_len = len(second_s)
            smaller = 2
        for i in range(smaller_len):
            result += (ord(first_s[index]) * ord(second_s[index]))
            index += 1
        if smaller == 1:
            for each in second_s[::(len(first_s))]:
                result += ord(each)
            result -= ord(second_s[0])  # TODO off by one issue
        elif smaller == 2:
            for each in first_s[::(len(second_s))]:
                result += ord(each)
            result -= ord(first_s[0])  # TODO off by one issue

    return result


string_input = input().split(" ")
print(char_multiplier(string_input[0], string_input[1]))
