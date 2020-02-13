

input_list = input().split()
first_digit_list = []

# take first digit
# compare first digits - sort reversed
# if there are even first digits: <--------------
#   - take bigger 2digit number
#   - take 2digit number
#   - take 1digit number

# take first digit
for each_item in input_list:
    first_digit = int(each_item[:1])
    first_digit_list.append(first_digit)


output_list = []
element_index = first_digit_list.index(max(first_digit_list))
# output_list.append(input_list[element_index])
print(element_index)
# output_list.append(max(first_digit_list))


print(input_list)
print(first_digit_list)


