# Create a program that calculates what percentage you’ve travelled.
# First, you will receive how many steps you’ve made.
# Then, you will receive how long 1 step is in centimeters.
# Last, you will receive the distance you need to travel in meters.
# Then you have to calculate what distance you have travelled with the steps given.
# Have in mind that every fifth step is 30% shorter than usual.
# You have to calculate what percentage of the distance you’ve travelled.
# In the end, print the percentage of the distance travelled,
# formatted to the 2nd decimal place, in the following format:
# "You travelled {percentage}% of the distance!"

steps = int(input())
step_length = float(input())
distance_meters = int(input())
covered_distance = 0

for i in range(1, steps + 1):
    if i % 5 == 0:
        covered_distance += 0.7 * step_length
    else:
        covered_distance += step_length

covered_distance_meters = covered_distance / 100
percentage = covered_distance / distance_meters

print(f"You travelled {percentage:.2f}% of the distance!")
