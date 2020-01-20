# Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best snowballs.
# They have decided to involve you in their fray, by making you write a program, which calculates snowball data,
# and outputs the best snowball value.
#
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# For each snowball you will receive 3 input lines:
# •	On the first line you will get the snowballSnow – an integer.
# •	On the second line you will get the snowballTime – an integer.
# •	On the third line you will get the snowballQuality – an integer.
# For each snowball you must calculate its snowballValue by the following formula:
# (snowballSnow / snowballTime) ^ snowballQuality
# At the end you must print the highest calculated snowballValue.

snowballs_amount = int(input())
snowball_value = 0
max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0

for counter in range(snowballs_amount):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    new_snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if new_snowball_value > snowball_value:
        snowball_value = new_snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {snowball_value:.0f} ({max_snowball_quality})")
