# Write a regular expression to match a valid phone number from Sofia.
# After you find all valid phones, print them on the console, separated by a comma and a space ", ".
# Example:
# Match ALL of these	        Match NONE of these
# +359 2 222 2222               359-2-222-2222, +359/2/222/2222, +359-2 222 2222
# +359-2-222-2222	            +359 2-222-2222,+359-2-222-222, +359-2-222-22222

import re


def find_phone_number(string):
    regex = r"(\+359([-| ])2\2\d{3}\2\d{4}\b)"
    # alternative RegEx that won't return tuple: r"\+359[ ]2[ ][\d]{3}[ ][\d]{4}\b|\+359[-]2[-][\d]{3}[-][\d]{4}\b"
    result = re.findall(regex, string)  # there are 2 groups in our RegEx, so a tuple will be returned
    return ", ".join([phone for phone, sep in result])  # the results from the first group of each tuple are joined


user_input = input()
print(find_phone_number(user_input))
