# Inbox Manager
# https://judge.softuni.bg/Contests/Practice/Index/1928#2

message = input()
users_dict = {}

while not message == "Statistics":
    command = message.split("->")[0]
    username = message.split("->")[1]
    if command == "Add":
        if username not in users_dict:
            users_dict[username] = []
        else:
            print(f"{username} is already registered")

    elif command == "Send":
        email = message.split("->")[2]
        users_dict[username].append(email)

    elif command == "Delete":
        if username in users_dict.keys():
            del users_dict[username]
        else:
            print(f"{username} not found!")

    message = input()

users_dict = dict(sorted(users_dict.items(), key=lambda u: (-len(u[1]), u[0])))

print(f"Users count: {len(users_dict.keys())}")
for each_user in users_dict.keys():
    print(f"{each_user} ")
    for each_mail in users_dict[each_user]:
        print(f"- {each_mail}")
