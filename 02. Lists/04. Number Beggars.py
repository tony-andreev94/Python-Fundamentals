#

numbers = [int(x) for x in input().split(", ")]  # 1 2 3 4 5
beggars = int(input())  # 3
target_list = []

# 1 2 3 4 5  / 3
# beg1 - 1, 4
# beg2 - 2, 5
# beg3 - 3

for iterations in range(beggars):
    target_list.insert(iterations, 0)
    print(iterations)  # 0 1 2
    # 0
    for item in numbers:  # 1 2 3 4 5
        #increase_value = item[0]
        target_list[iterations] += item

# list1 = []
# for i in range(5):
#     list1[i] = list1[i] + 2*i
# https://stackoverflow.com/questions/16903264/basic-python-how-to-increase-value-of-item-in-list

print(target_list)




# na bazata na vseki index da uvelichava razlichna suma
# b = 5
#
# print(0 % b)
# print(1 % b)
# print(2 % b)
# print(3 % b)
# print(4 % b)
# print(5 % b)
