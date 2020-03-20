# Nakov likes Math. But he also likes the English alphabet a lot.
# He invented a game with numbers and letters from the English alphabet. The game was simple.
# You get a string consisting of a number between two letters. Depending on whether the letter was in front
# of the number or after it you would perform different mathematical operations on the number to achieve the result.
# First you start with the letter before the number.
# •	If it's uppercase you divide the number by the letter's position in the alphabet.
# •	If it's lowercase you multiply the number with the letter's position in the alphabet.
# Then you move to the letter after the number.
# •	If it's uppercase you subtract its position from the resulted number.
# •	If it's lowercase you add its position to the resulted number.
# But the game became too easy for Nakov really quick. He decided to complicate it a bit by doing the same but
# with multiple strings keeping track of only the total sum of all results.


def find_alphabet_position(letter):
    if 65 <= ord(letter) <= 90:
        letter_position = ord(letter) - 64
    elif 97 <= ord(letter) <= 122:
        letter_position = ord(letter) - 96

    return letter_position


def find_string_sum(string):
    current_sum = 0
    # work with first letter
    if 65 <= ord(string[0]) <= 90:  # check if uppercase or lowercase
        current_sum = int(string[1:-1]) / find_alphabet_position(string[0])  # redundant check for ASCII value
    elif 97 <= ord(string[0]) <= 122:
        current_sum = int(string[1:-1]) * find_alphabet_position(string[0])  # redundant check for ASCII value

    # work with second letter
    if 65 <= ord(string[-1]) <= 90:  # check if uppercase or lowercase
        current_sum -= find_alphabet_position(string[-1])
    elif 97 <= ord(string[-1]) <= 122:
        current_sum += find_alphabet_position(string[-1])

    return current_sum


def find_total_sum(string):
    total_sum = 0
    work_list = string.split() # by splitting with .split() the split is done by all whitespace and not just by " "
    for each in work_list:
        total_sum += find_string_sum(each)

    return f"{total_sum:.2f}"


user_input = input()
print(find_total_sum(user_input))
