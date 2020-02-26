# Biscuits Factory

# Take input
biscuits = int(input())  # per worker
workers = int(input())
competition_biscuits = int(input())  # total, per month
daily_biscuits = biscuits * workers
total_biscuits = 0

for days in range(1, 31):
    if days % 3 == 0:
        total_biscuits += int(0.75 * daily_biscuits)
    else:
        total_biscuits += daily_biscuits

print(f"You have produced {total_biscuits} biscuits for the past month.")

percentage = abs((total_biscuits - competition_biscuits)/competition_biscuits * 100)

if total_biscuits > competition_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
