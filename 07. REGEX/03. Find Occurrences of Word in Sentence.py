# Write a program that finds, how many times a given word, is used in a given sentence.
# Note that letter case does not matter – it is case-insensitive.
# The output is a single number indicating the amount of times the sentence contains the word.

import re


def find_word(string, word):
    regex = build_regex(word)
    result = re.findall(regex, string, re.IGNORECASE)
    return len(result)


def build_regex(word):
    regex = ""
    for char in word:
        regex += f"[{char}]"
    regex += r"\W"  # add this to the regex, so that parts of words are not considered a match (there in therefore)
    return regex


user_input = input()
word = input()
print(find_word(user_input, word))

