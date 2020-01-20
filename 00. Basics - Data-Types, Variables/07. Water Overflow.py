# You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water,
# which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!"
# and continue reading the next line. On the last line, print the liters in the tank.
#
# Input	        Output
# 5
# 20
# 100
# 100
# 100           Insufficient capacity!
# 20	        240

counter = int(input())
max_capacity = 255
current_capacity = 0

for i in range(counter):
    water_input = int(input())
    if current_capacity + water_input <= max_capacity:
        current_capacity += water_input
    else:
        print('Insufficient capacity!')
print(current_capacity)
