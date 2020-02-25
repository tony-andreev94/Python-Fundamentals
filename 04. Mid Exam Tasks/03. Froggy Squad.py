# Create a program that helps you keep track of the frogs that are on the riverside.
# Because you are an extreme animal lover, you also name them.
# You will receive the names of the frogs that are already on the riverside on a single line,
# separated by a single space in the following format:
# "{frog1} {frog2} {frog3}… {frogn}"
# Then you will receive commands that describe their action. There are five possible commands:

frog_names = input().split(' ')

while True:
    command = input().split(' ')
    if command[0] == 'Join':
        frog_names.append(command[1])
    if command[0] == 'Jump':
        frog_names.insert(int(command[2]), command[1])
    if command[0] == 'Dive':
        # Check index
        frog_names.remove(frog_names[int(command[1])])
    if command[0] == 'First':
        for index in range(int(command[1])):
            print(frog_names[index], end=" ")
            if index == len(frog_names) - 1:
                break
    if command[0] == 'Last':
        for index in range(-1, -(int(command[1]) + 1), -1):
            print(frog_names[index], end=" ")
            if index == len(frog_names) - 1:
                break
    if command[0] == 'Print':
        print()
        print("Frogs:", end=" ")
        if command[1] == 'Normal':
            for each_frog in frog_names:
                print(each_frog, end=" ")
            break

        if command[1] == 'Reversed':
            for each_frog in reversed(frog_names):
                print(each_frog, end=" ")
            break
