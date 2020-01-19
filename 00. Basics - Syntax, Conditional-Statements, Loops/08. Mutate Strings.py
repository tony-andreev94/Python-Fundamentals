# You will be given two strings. Transform the first string into the second one, one letter at a time and print it.
# Print only the unique strings
# Note: the strings will have the same lengths
# Input	        Output
# Kitty         Ditty
# Doggy	        Dotty
#               Dogty
#               Doggy

first_string = input()
target_string = input()
counter = 0
work_list = list(first_string)

for i in target_string:
    work_list[counter] = i
    counter += 1
    if i != first_string[counter - 1]:
        print("".join(work_list))
    else:
        continue
