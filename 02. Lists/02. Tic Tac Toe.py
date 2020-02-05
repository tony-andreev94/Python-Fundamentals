# You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins print "First player won",
# otherwise if the second player wins print "Second player won", otherwise print "Draw!"
#
# Input	        Output
# 2 0 1         First player won
# 0 1 0
# 1 0 2
#
# 0 1 0         Second player won
# 2 2 2
# 1 0 0

first_row = [int(x) for x in input().split()]
second_row = [int(x) for x in input().split()]
third_row = [int(x) for x in input().split()]

if (first_row[0] == first_row[1] == first_row[2] == 1) or (second_row[0] == second_row[1] == second_row[2] == 1) or (
        third_row[0] == third_row[1] == third_row[2] == 1) or (first_row[0] == second_row[0] == third_row[0] == 1) or (
        first_row[1] == second_row[1] == third_row[1] == 1) or (first_row[2] == second_row[2] == third_row[2] == 1) or (
        first_row[0] == second_row[1] == third_row[2] == 1) or (first_row[2] == second_row[1] == third_row[0] == 1):
    print(f"First player won")
elif (first_row[0] == first_row[1] == first_row[2] == 2) or (second_row[0] == second_row[1] == second_row[2] == 2) or (
        third_row[0] == third_row[1] == third_row[2] == 2) or (first_row[0] == second_row[0] == third_row[0] == 2) or (
        first_row[1] == second_row[1] == third_row[1] == 2) or (first_row[2] == second_row[2] == third_row[2] == 2) or (
        first_row[0] == second_row[1] == third_row[2] == 2) or (first_row[2] == second_row[1] == third_row[0] == 2):
    print(f"Second player won")
else:
    print("Draw!")
