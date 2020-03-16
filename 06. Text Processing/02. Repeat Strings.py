# Write a Program That Reads a list of strings. Each string is repeated N times, where N is the length of the string.
# Print the concatenated string.
# Input	            Output
# hi abc add	    hihiabcabcabcaddaddadd
# work	            workworkworkwork
# ball	            ballballballball


def multiply_by_length(string):
    items_list = string.split(" ")
    return "".join(each_item * len(each_item) for each_item in items_list)


def multiply_by_length_2(string):
    """
    An alternative solution.
    """
    items_list = string.split(" ")
    result = ""
    for each_item in items_list:
        result += each_item * len(each_item)

    return result


print(multiply_by_length(input()))  # test first function
print(multiply_by_length_2(input()))  # test second function
