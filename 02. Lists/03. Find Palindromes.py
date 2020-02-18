# Write a program that receives on the first line words separated by a space and a searched palindrome on the second
# Print all the palindromes on the first line
# Print all the occurrences of the searched palindrome in the format:
# "Found palindrome {count} times"

words_input = input().split(" ")
searched_word = input()
palindrome_list = []

for each_item in words_input:
    reversed_word = each_item[::-1]
    if each_item == reversed_word:
        palindrome_list.append(each_item)

print(palindrome_list)
print(f"Found palindrome {words_input.count(searched_word)} times")
