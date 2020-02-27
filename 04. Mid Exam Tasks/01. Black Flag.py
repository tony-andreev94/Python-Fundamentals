# Create a program that checks if a target plunder is reached. First you will receive how many days the pirating lasts.
# Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.
# Calculate how much plunder the pirates manage to gather. Each day they gather plunder.
# Keep in mind that every third day they attack more ships and they add additional plunder
# to their total gain which is 50% of the daily plunder.
# Every fifth day the pirates encounter a warship and after the battle they lose 30% of their total plunder.
# If the gained plunder is more or equal to the target print the following:
#   "Ahoy! {totalPlunder} plunder gained."
# If the gained plunder is less than the target. Calculate the percentage left and print the following:
#   "Collected only {percentage}% of the plunder."
# Both numbers should be formatted to the 2nd decimal place.

days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for i in range(1, days + 1):
    if i % 3 == 0:
        total_plunder += 1.5 * daily_plunder

    if i % 5 == 0:
        if not i % 3 == 0:
            total_plunder += daily_plunder
        total_plunder = 0.7 * total_plunder

    if not i % 3 == 0 and not i % 5 == 0:
        total_plunder += daily_plunder

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")


