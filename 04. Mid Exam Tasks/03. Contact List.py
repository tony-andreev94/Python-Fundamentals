# Create a program that helps you keep track of the contacts that you have.
# You will receive the list of contacts you already have on a single line,
# separated by a single space in the following format:
# "{contact1} {contact2} {contact3}… {contactn}"
# Then you will receive commands that you need to execute over your list. There are four possible commands:
# •	"Add {contact} {index}":
# o	If {contact} isn’t already contained – add it in the end of the collection.
# o	If {contact} is already contained – add it on the given index, if the index exists.
# •	"Remove {index}"
# o	Remove the contact on the given index, if the index exists.
# •	"Export {startIndex} {count}":
# o	Print the next {count} contacts starting from the given {startIndex} (including),
# separated by a single space. If the count requested is more than the contacts- just print them to the end.
# "{contact} {contact} {contact}"
# •	"Print Normal/Reversed"
# o	Print the contact list in normal (in the order they have been added) or reversed order and then stop the program:
# "Contacts: {contact1} {contact2}… {contactn}"

contact_list = input().split(" ")
command = input().split(" ")
exported_contacts = []

while True:
    if command[0] == "Add":
        if command[1] not in contact_list:
            contact_list.append(command[1])
        else:
            if 0 <= int(command[2]) < len(contact_list):
                contact_list.insert(int(command[2]), command[1])

    elif command[0] == "Remove":
        if 0 <= int(command[1]) < len(contact_list):
            contact_list.pop(int(command[1]))

    elif command[0] == "Export":
        if 0 <= int(command[1]) < len(contact_list) and int(command[1]) + int(command[2]) < len(contact_list):
            for i in range(int(command[1]), int(command[1]) + int(command[2])):
                exported_contacts.append(contact_list[i])
            print(" ".join(exported_contacts))
            exported_contacts = []

        elif 0 <= int(command[1]) < len(contact_list) and int(command[1]) + int(command[2]) >= len(contact_list):
            exported_contacts = contact_list[int(command[1]):]
            print(" ".join(exported_contacts))
            exported_contacts = []

    elif command[0] == "Print":
        if command[1] == "Normal":
            print(f'Contacts: {" ".join(contact_list)}')
            break
        elif command[1] == "Reversed":
            print(f'Contacts: {" ".join(contact_list[::-1])}')
            break

    command = input().split(" ")
