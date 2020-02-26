# Wizard Poker

# Take input:
all_cards = input().split(":")
command = input().split(" ")
deck = []

while not command[0] == "Ready":
    if command[0] == "Add":
        if command[1] in all_cards:
            deck.append(command[1])
        else:
            print(f"Card not found.")

    elif command[0] == "Insert":
        if command[1] in all_cards and 0 <= int(command[2]) < len(deck):
            deck.insert(int(command[2]), command[1])
        else:
            print(f"Error!")

    elif command[0] == "Remove":
        if command[1] in deck:
            deck.remove(command[1])
        else:
            print(f"Card not found.")

    elif command[0] == "Swap":
        index_1 = deck.index(command[1])
        index_2 = deck.index(command[2])
        deck[int(index_1)], deck[int(index_2)] = deck[int(index_2)], deck[int(index_1)]

    elif command[0] == "Shuffle":
        deck = deck[::-1]

    command = input().split(" ")

# Print the result
result = " ".join(deck)
print(result)


