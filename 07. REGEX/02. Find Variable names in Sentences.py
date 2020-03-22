# Write a program that finds all variable names in a given string. A variable name starts with an underscore ("_")
# and contains only Capital and Non-Capital English Alphabet letters and digits.
# Extract only their names, without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names, extracted and printed on a single line, each separated by a comma.

import re


def find_variables(string):
    regex = r"(?<= _)[A-Za-z0-9]+(?=\s|$)"  # check note
    result = re.finditer(regex, string)
    return ",".join(each.group(0) for each in result)


user_input = input()
print(find_variables(user_input))

# __invalidVariable _evenMoreInvalidVariable_ _validVariable   ---> validVariable
# positive lookbehind is used to check if there is only one preceding "_"                                   (?<= _)
# and positive lookahead was used # to check there is a whitespace or end of sting after the variable       (?=\s|$)
