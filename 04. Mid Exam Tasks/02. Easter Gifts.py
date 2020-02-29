# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying оn a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
# •	"Required {gift} {index}"
# o	Replace the value of the current gift on the given index with this gift, if the index is valid.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"

gifts = input().split(" ")
command = input().split(" ")
result_list = []

while command[0] != "No":
    if command[0] == "OutOfStock":
        while command[1] in gifts: #while loop
            index_value = gifts.index(command[1])
            gifts[index_value] = "None"

    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(" ")

for each_gift in gifts:
    if not each_gift == "None":
        result_list.append(each_gift)

print(" ".join(result_list))
