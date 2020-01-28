# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee,
# and the team with less than 7 players loses.
#
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number.
# e.g. the card 'B-7' means player #7 from team B received a card. (index 6 of the list)
# The task: Given a list of cards (could be empty), return the number of remaining players on each team
# at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}".
# If the game was terminated print an additional line: "Game was terminated"
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.
# Input	                                Output
# A-1 A-5 A-10 B-2	                    Team A - 8; Team B - 10
# A-1 A-5 A-10 B-2 A-10 A-7 A-3	        Team A - 6; Team B - 10
#                                       Game was terminated

input_list = input().split()      # A-1 A-5 A-10 B-2
# A set is created so we can "ignore" duplicate input about already sent off players
my_set = set(input_list)
players_a = 11
players_b = 11
is_terminated = False

for each_item in my_set:
    if 'A-' in each_item:
        players_a -= 1
    # else:
    #     players_b -= 1
    elif 'B-' in each_item:
        players_b -= 1
    if players_a == 6 or players_b == 6:
        is_terminated = True
        break

print(f"Team A - {players_a}; Team B - {players_b}")
if is_terminated:
    print("Game was terminated")

