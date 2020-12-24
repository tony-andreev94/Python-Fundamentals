#3
guest_meals_collection = {}
unliked_meals = 0

command = input()
while not command == "Stop":
    parts = command.split('-')
    command = parts[0]
    guest = parts[1]#[1:-1]
    meal = parts[2]#[1:-1]
    if command == 'Like':
        if guest in guest_meals_collection.keys():
            if meal not in guest_meals_collection[guest]:
                guest_meals_collection[guest].append(meal)
        else:
            guest_meals_collection[guest] = []
            guest_meals_collection[guest].append(meal)

    if command == 'Unlike':
        if guest not in guest_meals_collection.keys():
            print(f"{guest} is not at the party.")
        else:
            if meal not in guest_meals_collection[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            elif meal in guest_meals_collection[guest]:
                unliked_meals += 1
                guest_meals_collection[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")

    command = input()

# format oder for printing

#sort
guest_meals_collection = dict(sorted(guest_meals_collection.items(), key=lambda g: (-len(g[1]), g[0])))

for key, value in guest_meals_collection.items():
    print(f"{key}: {', '.join(value)}")

#print(guest_meals_collection)
print(f"Unliked meals: {unliked_meals}")

