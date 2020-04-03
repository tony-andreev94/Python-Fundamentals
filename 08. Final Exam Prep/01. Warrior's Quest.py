# TODO - 90/100
# revisit
skill = input()
command = input().split()

while command[0] != "For":
    if command[0] == 'GladiatorStance':
        gladiator = skill.upper()
        skill = gladiator
        print(skill)
    elif command[0] == 'DefensiveStance':
        defensive = skill.lower()
        skill = defensive
        print(skill)
    elif command[0] == "Dispel":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(skill):
            new_skill = skill[:index] + letter + skill[index + 1:]
            skill = new_skill
            print("Success!")
        else:
            print("Dispel too weak.")
        pass
    elif command[0] == "Target":
        if command[1] == "Change":
            old = command[2]
            new = command[3]
            if old in skill:
                new_skill = skill.replace(old, new)
                skill = new_skill
                print(skill)

        elif command[1] == "Remove":
            text_strip = command[2]
            if text_strip in skill:
                new_skill = skill.replace(text_strip, "")
                skill = new_skill
                print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")

    command = input().split()
