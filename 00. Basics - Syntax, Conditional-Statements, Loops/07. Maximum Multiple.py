# Given a Divisor and a Bound, find the largest integer N, such that:
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found
# Input	        Output
# 2             6
# 7
#
# 10            50
# 50
#
# 37            185
# 200

divisor = int(input())
bound = int(input())
max_n = 0

for i in range(divisor, bound+1):
    if i % divisor == 0:
        max_n = i

print(max_n)
