# School library

# Take input
bookshelf = input().split('&')
command = input().split(' | ')

# Logic loop
while not command[0] == "Done":
    if command[0] == "Add Book":
        if command[1] not in bookshelf:
            bookshelf.insert(0, command[1])

    elif command[0] == "Take Book":
        if command[1] in bookshelf:
            bookshelf.remove(command[1])

    elif command[0] == "Swap Books":
        if command[1] in bookshelf and command[2] in bookshelf:
            # Get index:
            first_index = bookshelf.index(command[1])
            second_index = bookshelf.index(command[2])
            # Swap places:
            bookshelf[first_index], bookshelf[second_index] = bookshelf[second_index], bookshelf[first_index]

    elif command[0] == "Insert Book":
        bookshelf.append(command[1])

    elif command[0] == "Check Book":
        if int(command[1]) < len(bookshelf):
            print(bookshelf[int(command[1])])

    command = input().split(" | ")

# Print output
result = ", ".join(bookshelf)
print(result)
