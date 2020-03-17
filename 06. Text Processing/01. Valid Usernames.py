# Write a program that reads user names on a single line (joined by ", ") and prints all valid usernames.
# A valid username is:
# •	Has length between 3 and 16 characters
# •	Contains only letters, numbers, hyphens and underscores
# •	Has no redundant symbols before, after or in between


def length_validation(username):
    if 3 < len(username) < 16:
        return True


def symbol_validation(username):
    is_valid = True
    for each_char in username:
        if not each_char.isalnum() and each_char not in "-_":
            is_valid = False
            break

    if is_valid:
        return True


def username_validation(usernames):
    result = ""
    for each_username in usernames:
        if length_validation(each_username) and symbol_validation(each_username):
            result += each_username + '\n'

    return result


username_list = input().split(", ")
print(username_validation(username_list))


