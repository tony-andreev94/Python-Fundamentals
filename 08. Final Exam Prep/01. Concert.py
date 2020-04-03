# Concert
# https://judge.softuni.bg/Contests/Practice/Index/1759#0

command = input().split("; ")
band_dict = {}
band_time = {}
total_time = 0  # I can take it as sum of all values of the "band_time" dictionary

while command[0] != "start of concert":
    word = command[0]
    if word == "Add":
        band = command[1]
        members_list = command[2].replace("'", "").split(", ")
        if band not in band_dict.keys():
            band_dict[band] = members_list
        else:
            old_members = band_dict[band]
            for each in members_list:
                if each not in old_members:
                    old_members.append(each)

    elif word == "Play":
        band = command[1]
        play_time = int(command[2])
        if band not in band_time.keys():
            band_time[band] = 0
            band_time[band] += play_time
        else:
            band_time[band] += play_time
        total_time += play_time

    command = input().split("; ")

band_name = input()

# First result:
print(f"Total time: {total_time}")
band_time = dict(sorted(band_time.items(), key=lambda t: -t[1]))
for band, time in band_time.items():
    print(f"{band} -> {time}")

# Second result:
most_played = next(iter(band_time))
print(most_played)
for each in band_dict[band_name]:
    print(f"=> {each}")
