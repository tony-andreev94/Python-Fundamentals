# Given two lists of strings print a new list of the strings that contains words from the first list
# which are substrings of any of the strings in the second list (only unique values)
#
# Input	                                    Output
# arp, live, strong                         ['arp', 'live', 'strong']
# lively, alive, harp, sharp, armstrong
#
# tarp mice bull                            []
# lively alive harp sharp armstrong

first_list = input().split(", ")
second_list = input().split(",")
target_list = []

for first_l_el in first_list:
    for second_l_el in second_list:
        str_value = str(first_l_el)

        if str_value in second_l_el:
            target_list.append(str_value)

# Remove duplicates
target_set = set(target_list)
print(list(target_set))
#print(list(set(target_list)))