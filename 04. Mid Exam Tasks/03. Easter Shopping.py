# Create a program that helps you keep track of the shops that you want to visit. You will receive the list of shops you have planned on checking out on a single line, separated by a single space in the following format:
# "{shop1} {shop2} {shop3}… {shopn}"
# Then you will receive a number – n - a count of commands you need to execute over your list. There are four possible commands:
# •	"Include {shop}":
# o	Add the shop at the end of your list.
# •	"Visit {first/last} {numberOfShops}"
# o	Remove either the "first" or the "last" number of shops from your list, depending on the input. If you have less shops on your list than the given number, skip this command.
# •	"Prefer {shopIndex1} {shopIndex2}":
# o	If both of the shop indexes exist in your list, take the shops that are on them and change their places.
# •	"Place {shop} {shopIndex}"
# o	Insert the shop after the given index, only if the resulted index exists.
# In the end print the manipulated list in the following format:
# "Shops left:
# {shop1} {shop2}… {shopn}"

shops = input().split(" ")
commands_count = int(input())

for i in range(commands_count):
    command = input().split(" ")
    if command[0] == "Include":
        shops.append(command[1])

    elif command[0] == "Visit":
        if int(command[2]) <= len(shops):
            if command[1] == "first":
                for index in range(int(command[2])):
                    shops.pop(0)
            elif command[1] == "last":
                for index in range(int(command[2])):
                    shops.pop(-1)

    elif command[0] == "Prefer":
        if 0 <= int(command[1]) < len(shops) and 0 <= int(command[2]) < len(shops):
            shops[int(command[1])], shops[int(command[2])] = shops[int(command[2])], shops[int(command[1])]

    elif command[0] == "Place":
        if 0 <= int(command[2]) < len(shops):
            shops.insert(int(command[2]) + 1, command[1])


print(f"Shops left:")
print(" ".join(shops))
