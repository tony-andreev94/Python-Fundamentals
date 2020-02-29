# Create a program that helps you keep track of a number array.
# First, you are going to receive the numbers оn a single line, separated by space, in the following format:
# "{number1} {number2} {number3}… {numbern}"
# Then you will start receiving commands until you read the "End" message. There are five possible commands:
# •	"Switch {index}"
#   oFind the number on this index in your collection, if the index exists, and switch its sign (negative <-> positive).
# •	"Change {index} {value}"
#   oReplace the number on the given index with the number given, if the index exists.
# •	"Sum Negative"
#   oPrint the sum of all negative numbers.
# •	"Sum Positive"
#   oPrint the sum of all positive numbers.
# •	"Sum All"
#   oPrint the sum of all numbers.
# In the end, print the positive numbers on a single line, keeping in mind that 0 is positive,
# separated by a single space in the following format:
# "{number1} {number2} {number3}… {numbern}"

input_array = [int(x) for x in input().split(" ")]
command = input().split(" ")

negative_sum = 0
positive_sum = 0
all_sum = 0
result_list = []

while command[0] != "End":
    if command[0] == "Switch":
        if 0 <= int(command[1]) < len(input_array):
            input_array[int(command[1])] *= -1

    elif command[0] == "Change":
        if 0 <= int(command[1]) < len(input_array):
            input_array[int(command[1])] = int(command[2])

    elif command[0] == "Sum":
        for each_item in input_array:
            all_sum += each_item
            if each_item < 0:
                negative_sum += each_item
            elif each_item >= 0:
                positive_sum += each_item

        if command[1] == "Negative":
            print(negative_sum)
        elif command[1] == "Positive":
            print(positive_sum)
        elif command[1] == "All":
            print(all_sum)

    command = input().split(" ")

for each in input_array:
    if each >= 0:
        result_list.append(each)

print(*result_list)
