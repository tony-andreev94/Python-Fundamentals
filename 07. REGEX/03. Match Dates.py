# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.
import re


def find_dates(string):
    regex = r"(?P<day>\d{2})([.\-/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4})"
    # result = re.findall(regex, string)
    result = re.finditer(regex, string)
    return result


def format_output(list):
    for each in list:
        # print(f"Day: {each[0]}, Month: {each[2]}, Year: {each[3]}")
        print(f"Day: {each.group('day')}, Month: {each.group('month')}, Year: {each.group('year')}")


user_input = input()
format_output(find_dates(user_input))
