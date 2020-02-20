# You will receive a single line containing numbers separated by a single space.
# Form the biggest number possible from them

# Input	                    Output	        Comment
# 3 30 34 5 9	            9534303	        The numbers sorted are 9 5 34 30 3
# 1 2 3	                    321

input_list = input().split()
first_digit_list = []

for each_item in list(reversed(sorted(input_list))):
    print(each_item, end="")


