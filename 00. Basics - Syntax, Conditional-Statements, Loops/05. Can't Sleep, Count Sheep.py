# If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a murmur:
# "1 sheep...2 sheep...3 sheep..."
# Input will always be valid, i.e. no negative integers.
#
# Input	        Output
# 5	            1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...
# 1	            1 sheep...

sheep_counter = int(input())

for i in range(1, sheep_counter + 1):
    print(f"{i} sheep...", end="")
