# Write a program that takes a text and a string of banned words.
# All words included in the ban list should be replaced with asterisks "*", equal to the word's length.
# The entries in the ban list will be separated by a comma and space ", ".
# The ban list should be entered on the first input line and the text on the second input line.
# TODO: do another solution with filter()


def filter_func(banned_words, text):
    for each_word in banned_words:
        if each_word in text:
            new_text = text.replace(each_word, '*' * len(each_word))
            text = new_text

    return text


banned_list = input().split(", ")
unfiltered_text = input()

print(filter_func(banned_list, unfiltered_text))
