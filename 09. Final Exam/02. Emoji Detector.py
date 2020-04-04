# Emoji Detector
# https://judge.softuni.bg/Contests/Compete/Index/2302#1
# TODO 70/100

import re


def multiply(input_list):
    result = 1
    for each_digit in input_list:
        result *= each_digit
    return result


def cool_emoji(input_list, cool_factor):
    cool_emojis = []
    for each in input_list:
        emoji = each.strip(':*')
        if sum([ord(char) for char in emoji]) >= cool_factor:
            cool_emojis.append(each)
    return cool_emojis


text = input()
emoji_regex = r"([:*]{2})([A-Z][a-z]{2,})\1"
digit_regex = r"\d"

e_match = re.findall(emoji_regex, text)
d_match = re.findall(digit_regex, text)

digits_list = [int(each) for each in d_match]
full_emoji = [str(each[0] + each[1] + each[0]) for each in e_match]
cool_factor = multiply(digits_list)
cool_emojis = cool_emoji(full_emoji, cool_factor)

print(f"Cool threshold: {cool_factor}")

print(f"{len(full_emoji)} emojis found in the text. The cool ones are:")
for each in cool_emojis:
    print(each)