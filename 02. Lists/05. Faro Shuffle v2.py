# A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half
# and then the cards in the two halves are perfectly interwoven,
# such that the original bottom card is still on the bottom and the original top card is still on top.
#
# Input	                    Output
# a b c d e f g h           ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
# 5
#
# one two three four        ['one', 'three', 'two', 'four']
# 3

# Simpler solution
cards = input().split()  # 1 2 3 4 5 6
iterations = int(input()) # 1
half = len(cards) / 2  # for index it should be half - 1

for i in range(iterations):
    output_list = list()
    for j in range(int(half)):
        # j = 0, 1, 2   half = 3
        output_list.append(cards[j])
        output_list.append(cards[j + int(half)])
    cards = output_list
print(output_list)
