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

cards = input().split(" ")
shuffles = int(input())

last_element_index = len(cards) - 1

for iteration in range(shuffles):
    first_element = cards.pop(0)
    last_element = cards.pop()
    first_half = [1]
    second_half = []
    for i in range(int(len(cards) / 2)):
        element = cards.pop(0)
        first_half.insert(-1, element)

    first_half.pop()  # TODO temporary solution, fix it later
    second_half = cards

    target_list = []
    for counter in range(len(first_half)):
        first_h_item = first_half.pop(0)
        second_h_item = second_half.pop(0)

        target_list.append(second_h_item)
        target_list.append(first_h_item)

    target_list.insert(0, first_element)
    target_list.insert(last_element_index, last_element)
    # end
    cards = target_list


print(target_list)
