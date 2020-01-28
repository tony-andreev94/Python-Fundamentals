# This is a solution of the same task, but according to softuni's simplified scenario.
# Always only the head and tail are reversed.

tail = input()
body = input()
head = input()

# list = [tail, body, head]
# list[0], list[2] = list[2], list[0]
list = [head, body, tail]
print(list)
