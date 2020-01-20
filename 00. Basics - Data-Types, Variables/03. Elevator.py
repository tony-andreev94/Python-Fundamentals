# Calculate how many courses will be needed to elevate n persons by using an elevator of capacity of p persons.
# The input holds two lines: the number of people n and the capacity p of the elevator.

people = int(input())
capacity = int(input())

if people % capacity == 0:
    print(f"{people / capacity:.0f}")
else:
    print(int(people / capacity) + 1)
