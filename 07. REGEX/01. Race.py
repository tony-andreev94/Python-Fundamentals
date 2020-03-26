# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info which will be some alphanumeric characters.
# In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and
# the sum of the digits is the distance he ran. So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
import re


def find_name(string):
    regex = r"[A-Z]|[a-z]"
    result = re.findall(regex, string)
    return "".join(result)


def find_distance(string):
    distance = 0
    regex = r"[0-9]"
    result = re.findall(regex, string)
    for each in result:
        distance += int(each)
    return distance


def add_participant(name):
    participants[name] = 0


def add_distance(name, number):
    if name in participants.keys():
        if participants[name] == 0:
            participants[name] = number
        else:
            participants[name] += number


def sort_and_print(dictionary):
    winners_list = []
    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        person = key
        winners_list.append(person)

    return f"1st place: {winners_list[0]}\n2nd place: {winners_list[1]}\n3rd place: {winners_list[2]}"


# Take list of people and build dictionary:
participants = {}
people = input().split(", ")
for each_person in people:
    add_participant(each_person)

# Take input for the race:
user_input = input()
while user_input != "end of race":
    person_name = find_name(user_input)
    distance_ran = find_distance(user_input)
    if person_name is not None:
        if person_name in participants:
            add_distance(person_name, distance_ran)

    user_input = input()

# Print winners:
print(sort_and_print(participants))
