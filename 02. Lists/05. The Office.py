# You Will Receive Two Lines of Input: a List of Employee's Happiness As String with Numbers
# Separated by a Single Space and a Happiness Improvement Factor (Single Number).
# Your Task is to Find Out If the Employees Are.
# Generally Happy in Their Office. To Do That You Have to Increase Their Happiness by Multiplying the All the Employee's Happiness (the Numbers from the List) by the Factor, Filter the Employees Which Happiness is Greater Than or Equal to the Average in the New List and Print the Result
# There are two types of output:
# •	If the half or more of the employees have happiness >= than the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
#
# Input	                Output	                                   Comment
# 1 2 3 4 2 1           Score 2/6. Employees are not happy!        After the mapping:
# 3                                                                3 6 9 12 6 3        (6.5)
# 	                                                               After the filtration:
#                                                                  9 12
#                                                                  2/6 people are happy, so the overall happiness is bad

# Shorter solution
happiness_input = list(int(x) for x in input().split(' '))
happy_factor = int(input())
mapped_list = list(map(lambda x: x * happy_factor, happiness_input))

average_happiness = sum(mapped_list) / len(mapped_list)

filtered_list = list(filter(lambda x: x >= average_happiness, mapped_list))

if len(filtered_list) >= len(mapped_list):
    print(f"Score: {len(filtered_list)}/{len(mapped_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(mapped_list)}. Employees are not happy!")


# # Long solution only with loops
# happiness_input = list(int(x) for x in input().split(' '))
# happy_factor = int(input())
#
# mapped_list = []
# result_list = []
# for each_item in happiness_input:
#     mapped_list.append(each_item * happy_factor)
#
# average_happiness = 0
# for each_element in mapped_list:
#     average_happiness += each_element
#
# average_happiness = average_happiness / len(mapped_list)
#
# for each_el in mapped_list:
#     if each_el >= average_happiness:
#         result_list.append(each_el)
#
# if len(result_list) >= len(mapped_list) / 2:
#     print(f"Score: {len(result_list)}/{len(mapped_list)}. Employees are happy!")
# else:
#     print(f"Score: {len(result_list)}/{len(mapped_list)}. Employees are not happy!")
#
