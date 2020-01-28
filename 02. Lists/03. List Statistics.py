# You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
# •	One with all the positives (including 0)
# •	One with all the negatives
# Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"

n = int(input())
positive_list = list()
negative_list = list()
count_positives = 0
sum_of_negatives = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
        count_positives += 1
    else:
        negative_list.append(number)
        sum_of_negatives += number

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")
