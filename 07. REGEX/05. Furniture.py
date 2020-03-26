# Write a program to calculate the total cost of different types of furniture. You will be given some lines of input until you receive the line "Purchase". For the line to be valid it should be in the following format:
# ">>{furniture name}<<{price}!{quantity}"
# The price can be floating point number or whole number. Store the names of the furniture and the total price. At the end print the each bought furniture on separate line in the format:
# "Bought furniture:
# {1st name}
# {2nd name}
# …"
# And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.
# TODO make the two print() methods into function(s)
import re


def prepare_input(string):
    regex = r">|<|!"
    result = re.split(regex, string)
    filtered_result = [each for each in result if each != ""]
    return filtered_result


def calculate_furniture(list):
    money_spent = 0
    if len(list) == 3:
        money_spent += float(list[2]) * float(list[1])
    return money_spent


def print_func(list):
    if len(list) == 3:
        print(list[0])


user_input = input()
total_money = 0
print("Bought furniture:")

while not user_input == "Purchase":
    print_func(prepare_input(user_input))
    total_money += calculate_furniture(prepare_input(user_input))
    user_input = input()

print(f"Total money spend: {total_money:.2f}")
