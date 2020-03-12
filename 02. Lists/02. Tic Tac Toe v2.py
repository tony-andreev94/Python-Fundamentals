# Tic-Tac-Toe 
# You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# Legend:
# ·         0 - empty space
# ·         1 - first player move
# ·         2 - second player move
# Find out who the winner is. If the first player wins print "First player won",
# If the second player wins print "Second player won", otherwise print "Draw!"


def check_for_winner(input_list):
    test_set = set(input_list)
    if len(test_set) == 1:
        if test_set == {1}:
            print(f"First player won")
            exit(0)
        elif test_set == {2}:
            print(f"Second player won")
            exit(0)


def add_combination(item_1, item_2, item_3):
    combinations_list = [int(item_1), int(item_2), int(item_3)]
    return combinations_list


# Take input
first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")
lists_to_check = []  # list with possible combinations

# Add all 8 possible combinations in one list
# rows
lists_to_check.append(add_combination(first_line[0], first_line[1], first_line[2])) # lambda function
lists_to_check.append(add_combination(second_line[0], second_line[1], second_line[2]))
lists_to_check.append(add_combination(third_line[0], third_line[1], third_line[2]))
# columns
lists_to_check.append(list(add_combination(third_line[0], second_line[0], third_line[0])))
lists_to_check.append(list(add_combination(third_line[1], second_line[1], third_line[1])))
lists_to_check.append(list(add_combination(third_line[2], second_line[2], third_line[2])))
# diagonals
lists_to_check.append(list(add_combination(first_line[0], second_line[1], third_line[2])))
lists_to_check.append(list(add_combination(first_line[2], second_line[1], third_line[0])))

# Check if we have winning combination and exit
for each_list in lists_to_check:
    check_for_winner(each_list)

# if no winning combination is found, print Draw!
print("Draw!")
