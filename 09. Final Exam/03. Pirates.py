# Pirates
# https://judge.softuni.bg/Contests/Compete/Index/2302#2

user_input = input()
cities = {}
while user_input != "Sail":
    city = user_input.split("||")[0]
    population = int(user_input.split("||")[1])
    gold = int(user_input.split("||")[2])
    if city not in cities.keys():
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

    user_input = input()

user_input = input()

while user_input != "End":
    command = user_input.split("=>")[0]
    town = user_input.split("=>")[1]
    if command == "Plunder":
        people = int(user_input.split("=>")[2])
        gold = int(user_input.split("=>")[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] == 0 or cities[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    elif command == "Prosper":
        gold = int(user_input.split("=>")[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    user_input = input()

print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")

cities = dict(sorted(cities.items(), key=lambda c: (-((c[1])[1]), c[0])))
for key, value in cities.items():
    print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")

