# You will receive a string with even integers, separated by a "@". This is our neighborhood.
# After that a series of Jump commands will follow, until you receive "Love!"
# Every house in the neighborhood needs a certain number of hearts delivered by Cupid,
# in order to be able to celebrate Valentine’s Day. Those needed hearts are indicated by the integers in the neighborhood.
# Cupid starts at the position of the first house (index 0) and must jump by a given length.
# The jump commands will be in this format:
# "Jump {length}".
# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2.
# If the needed hearts for a certain house become equal to 0 , print on the console
# "Place {houseIndex} has Valentine's day."
# If Cupid jumps to a house where the needed hearts are already 0, print on the console
# "Place {houseIndex} already had Valentine's day.".
# Keep in mind that Cupid can have a bigger jump length than the size of the neighborhood and if he does jump outside of it,
# he should start from the first house again.
# For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2.
# He will end up at index 2 and decrease the needed hearts there by 2: [6, 6, 4].
# Next he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0) and again decreases the needed hearts there: [4, 6, 4].
#
# Input
# •	On the first line you will receive a string with even integers separated by "@"
# – the neighborhood and the number of hearts for each house.
# •	On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".
#
# Output
# At the end print Cupid's last position and whether his mission was successful or not:
# •	"Cupid's last position was {lastPositionIndex}."
# •	If each house has had a Valentine's day, print:
# o	"Mission was successful."
# •	If not, print the count of all houses that didn`t celebrate a Valentine's Day:
# o	"Cupid has failed {houseCount} places."

# Input
neighborhood = [int(x) for x in input().split("@")]
command = input().split(" ")
cupid_position = 0  # used to store the index for next command

# Main loop
while command[0] != "Love!":

    if command[0] == "Jump":
        index = cupid_position + int(command[1])  # we get the index position using the jump value
        if int(index) >= len(neighborhood):
            index = 0

        if neighborhood[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            neighborhood[index] -= 2
            if neighborhood[index] == 0:
                print(f"Place {index} has Valentine's day.")

    cupid_position = index  # cupid's position is stored for the next jump calculation
    command = input().split(" ")

# Output
print(f"Cupid's last position was {index}.")
if len(set(neighborhood)) == 1 and neighborhood[0] == 0:
    # if a list consisting of only 0s is converted to a set it should have a a length of 1 and one element that is 0
    print(f"Mission was successful.")
else:
    house_count = 0  # counter for all houses which have heart value different than 0
    for each_item in neighborhood:
        if not each_item == 0:
            house_count += 1
    print(f"Cupid has failed {house_count} places.")
