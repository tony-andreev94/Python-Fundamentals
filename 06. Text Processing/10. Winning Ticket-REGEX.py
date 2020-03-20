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


def check_for_win(ticket):
    winning_symbols = ['@', '#', '$', '^']
    first_part = ticket[:10]
    second_part = ticket[10:]
    match_symbol = ''
    match_length = ""
    # TODO check with REGEX for at least 6 uninterrupted symbols in "first_part" and "second_part"

    pass


ticket_list = input().split(", ")
for each_ticket in ticket_list:
    if check_ticket_validity(each_ticket):
        print(check_for_win(each_ticket))
    else:
        print("invalid ticket")



