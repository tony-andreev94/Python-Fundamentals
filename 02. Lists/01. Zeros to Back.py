# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros and moves them to the back without messing up the other elements.
# Print the resulting integer list

# Input	                    Output
# 1, 0, 1, 2, 0, 1, 3	    [1, 1, 2, 1, 3, 0, 0]

input_list = [int(x) for x in input().split(", ")]
output_list = []

for each_item in input_list:
    if each_item == 0:
        input_list.remove(0)
        output_list.append(0)

input_list.extend(output_list)
print(input_list)

# for i in range(len(input_list)):
#     if input_list[i] == 0:
#         # .pop() breaks the indexes
#         zero_element = input_list.pop(i)
#         output_list.append(zero_element)
