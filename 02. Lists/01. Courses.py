# You will receive a single number n. On the next n lines you will receive names of courses.
# You have to create a list of them and print it.
# Input	               Output
# 2                    ['PB Python', 'PF Python']
# PB Python
# BF Python

courses_num = int(input())
courses_list = []
for i in range(courses_num):
    course = input()
    courses_list.append(course)

print(courses_list)
