# Automate a check for winning lottery tickets.
# You are given a collection of tickets separated by commas and spaces.
# You need to check every one of them if it has a winning combination of symbols.
# A valid ticket should have exactly 20 characters.
# The winning symbols are '@', '#', '$' and '^'. But in order for a ticket to be a winner the symbol should
# uninterruptedly repeat for at least 6 times in both the tickets left half and the tickets right half.
# For example, a valid winning ticket should be something like this:
# "Cash$$$$$$Ca$$$$$$sh"
# The left half "Cash$$$$$$" contains "$$$$$$", which is also contained in the tickets right half "Ca$$$$$$sh".
# A winning ticket should contain symbols repeating up to 10 times in both halves,
# which is considered a Jackpot (for example: "$$$$$$$$$$$$$$$$$$$$").


def check_ticket_validity(ticket):
    if len(ticket) == 20:
        return True
    else:
        return False


def find_length_and_symbol(text):
    winning_symbols = ['@', '#', '$', '^']
    match_symbol = ''
    match_length = 1
    for index in range(len(text)):
        if text[index] in winning_symbols:
            if index + 1 < len(text) and text[index] == text[index + 1]:
                match_length += 1
                match_symbol = text[index]

    if match_length > 5:
        return match_symbol * match_length
    else:
        return -1


def check_for_win(ticket):
    first_part = ticket[:10]
    second_part = ticket[10:]
    left = find_length_and_symbol(first_part)  # not the best variable name
    right = find_length_and_symbol(second_part)  # not the best variable name
    if left == -1 or right == -1:
        return f'ticket "{first_part}{second_part}" - no match'
    if len(left) >= 6 and len(right) >= 6 and left[0] == right[0]:
        symbol = left[0]
        smaller_length = min(len(left), len(right))
        # if find_length_and_symbol(first_part) == find_length_and_symbol(second_part) and find_length_and_symbol(
        #         first_part) != -1: # TODO - not ==, but both >5 and return the smaller one
        if len(find_length_and_symbol(first_part)) == 10:
            return f'ticket "{find_length_and_symbol(first_part) * 2}" - 10{find_length_and_symbol(first_part)[0]} Jackpot!'
        else:
            return f'ticket "{first_part}{second_part}" - {smaller_length}{symbol}'
    else:
        return f'ticket "{first_part}{second_part}" - no match'


ticket_list = input().split(", ")
for each_ticket in ticket_list:
    each_ticket = each_ticket.replace(" ", "")
    if check_ticket_validity(each_ticket):
        print(check_for_win(each_ticket))
    else:
        print("invalid ticket")
