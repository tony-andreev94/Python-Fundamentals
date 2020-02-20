# You will be given a version as in this example: "1.3.4".
# You have to find the next version and print it ("1.3.5" from the example).
# The only rule is that the numbers cannot be greater than 9.
# If that happens, set the current number to 0 and increase the number before it.
# Note: there will be no case where the first number will get greater than 9

# Input	    Output
# 1.2.3	    1.2.4
# 1.3.9	    1.4.0

version = list(int(x) for x in input().split('.'))
output_string = ""

# Increase number
for number in range(-1, -4, -1):
    version[number] += 1
    if version[number] == 10:
        version[number] = 0
    else:
        break

# Alternate solution for "Increase number"
version[-1] += 1
if version[-1] == 10:
    version[-1] = 0
    version[-2] += 1
    if version[-2] == 10:
        version[-2] = 0
        version[-3] += 1

# Get output/result string
for each_item in version:
    output_string += (str(each_item) + '.')

# Print result
print(output_string[:-1])
