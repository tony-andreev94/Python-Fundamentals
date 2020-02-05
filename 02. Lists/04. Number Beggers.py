# Your task here is pretty simple: given a list of numbers and an amount of beggars,
# you are supposed to return a list with the sum of what each beggar brings home,
# assuming they all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6,
# as the first one takes [1,3,5], the second collects [2,4].
# The same list with 3 beggars would have in turn have produced a better outcome for the second beggar: 5, 7 and 3,
# as they will respectively take [1, 4], [2, 5] and [3].
# Also note that not all beggars have to take the same amount of "offers",
# meaning that the length of the list is not necessarily a multiple of n; length can be even shorter,
# in which case the last beggars will of course take nothing (0).
#
# Input	                Output
# 1, 2, 3, 4, 5         [9, 6]
# 2
# 3, 4, 5, 1, 29, 4     [3, 4, 5, 1, 29, 4]
# 6

numbers_list = [int(x) for x in input().split(", ")]  # 1, 2, 3, 4, 5
beggars = int(input())  # 3
output_list = []

for i in range(beggars):
    output_list.append(0)

# output_list = [0, 0, 0]

index = 0
for each_item in numbers_list:
    output_list[index] += each_item
    index += 1
    if index > len(output_list) - 1:
        index = 0

print(output_list)  # [5, 7, 3]
