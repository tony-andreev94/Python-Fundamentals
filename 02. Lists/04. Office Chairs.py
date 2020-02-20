# You will be given a number n representing how many rooms there are.
# On the next n lines for each room you will get how many chairs there are and how many of them will be taken.
# The chairs will be represented by "X"s, then there will be a space " " and a number representing the taken places.
# Example: "XXXXX 4" (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later.
# However if you get to a room where there are more people than chairs, print the following message:
#       "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
# If there is enough chairs in each room print:
#       "Game On, {total_free_chairs} free chairs left"

# Input	                Output
# 4                     Game On, 4 free chairs left
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3
#
# 3
# XXXXXXX 5
# XXXX 5                1 more chairs needed in room 2
# XXXXXX 8	            2 more chairs needed in room 3

rooms = int(input())
available_chairs = 0
enough_chairs = True

for room_number in range(1, rooms + 1):
    current_room = input().split(" ")
    chairs = current_room[0].count('X')
    if chairs >= int(current_room[1]):
        available_chairs += chairs - int(current_room[1])
    elif chairs < int(current_room[1]):
        enough_chairs = False
        print(f"{int(current_room[1]) - chairs} more chairs needed in room {room_number} ")

if enough_chairs:
    print(f"Game On, {available_chairs} free chairs left")

