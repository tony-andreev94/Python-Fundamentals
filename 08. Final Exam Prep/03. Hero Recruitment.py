# TODO sort the dictionary before printing:
# Print all the heroes sorted by their count of spells in descending
# and then by the hero name ascending in the format described below:
# revisit

hero_dict = {}
command = input().split()

while command[0] != "End":
    if command[0] == "Enroll":
        hero = command[1]
        if hero in hero_dict:
            print(f"{hero} is already enrolled.")
        else:
            hero_dict[hero] = []
    elif command[0] == "Learn":
        hero = command[1]
        spell = command[2]
        if hero not in hero_dict:
            print(f"{hero} doesn't exist.")
        elif spell in hero_dict[hero]:
            print(f"{hero} has already learnt {spell}.")
        else:
            hero_dict[hero].append(spell)
    elif command[0] == "Unlearn":
        hero = command[1]
        spell = command[2]
        if hero not in hero_dict:
            print(f"{hero} doesn't exist.")
        elif spell not in hero_dict[hero]:
            print(f"{hero} doesn't know {spell}")
        else:
            hero_dict[hero].remove(spell)

    command = input().split()


# Print results:
print("Heroes:")
# for key in hero_dict.keys():
#     print(f"== {key}: {', '.join(hero_dict[key])}")
for key in sorted(hero_dict):  # sorts only by key
    print(f"== {key}: {', '.join(hero_dict[key])}")

