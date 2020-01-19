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

for counter in range(bound, divisor - 1, -1):
    if counter % divisor == 0:
        print(counter)
        break

