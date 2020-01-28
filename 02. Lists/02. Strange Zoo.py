# You are at the zoo and the meerkats look strange. You will receive 3 strings: (tail, body, head).
# You have to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail)
# Input	                            Output
# my tail                           ['my head is on the wrong end!','my body seems on place','my tail']
# my body seems on place
# my head is on the wrong end!

# Defining the input:
first_string = input()
second_string = input()
third_string = input()
# the list of input strings
list_of_strings = list()
list_of_strings.append(first_string)
list_of_strings.append(second_string)
list_of_strings.append(third_string)
# the target list with placeholder values which will be overwritten, they are added so we can work with indexes
ordered_list = ['head', 'body', 'tail']

for i in list_of_strings:
    if 'head' in i:
        ordered_list[0] = i
    if 'body' in i:
        ordered_list[1] = i
    if 'tail' in i:
        ordered_list[2] = i

print(ordered_list)
