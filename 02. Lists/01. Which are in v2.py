# Given two lists of strings print a new list of the strings that contains words from the first list
# which are substrings of any of the strings in the second list (only unique values)
#
# Input	                                    Output
# arp, live, strong                         ['arp', 'live', 'strong']
# lively, alive, harp, sharp, armstrong
#
# tarp, mice, bull                          []
# lively, alive, harp, sharp, armstrong

first_list = input().split(', ')
second_list = input().split(', ')

result_list = list()

for each_item in first_list:
    for each_element in second_list:
        if each_item in each_element:
            result_list.append(each_item)

if len(result_list) == 0:
    print(result_list)
else:
    print(list(set(result_list)))

