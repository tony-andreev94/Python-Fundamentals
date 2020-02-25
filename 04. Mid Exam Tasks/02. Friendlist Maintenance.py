# Friendlist maintenance

friends_list = input().split(', ')
command = input().split(' ')
blacklisted_count = 0
lost_count = 0

while not command[0] == 'Report':
    if command[0] == 'Blacklist':
        if command[1] in friends_list:
            index = friends_list.index(command[1])
            friends_list[index] = 'Blacklisted'
            print(f"{command[1]} was blacklisted.")
            blacklisted_count += 1
        else:
            print(f"{command[1]} was not found.")
    if command[0] == 'Error':
        if friends_list[int(command[1])] == 'Blacklisted' or friends_list[int(command[1])] == 'Lost':
            pass
        else:
            print(f"{friends_list[int(command[1])]} was lost due to an error.")
            friends_list[int(command[1])] = 'Lost'
            lost_count += 1
    if command[0] == 'Change':
        if int(command[1]) < len(friends_list):
            print(f"{friends_list[int(command[1])]} changed his username to {command[2]}.")
            friends_list[int(command[1])] = command[2]
    command = input().split(' ')

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
for each_item in friends_list:
    print(each_item, end=" ")
