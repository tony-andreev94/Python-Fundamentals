# You're saying good-bye your best friend, "See you next happy year".
# Happy Year is the year with only distinct digits, (e.g) 2018.
# Write a program that receives an integer number and finds the next happy year.

# Input	        Output
# 8989	        9012
# 1001	        1023

current_year = int(input())
is_happy_year = False

while not is_happy_year:
    current_year += 1
    # Adding a desired number variable so that the program works fine with non-four digit years
    desired_number = len(list(str(current_year)))
    if len(set(str(current_year))) == desired_number:
        print(current_year)
        is_happy_year = True
