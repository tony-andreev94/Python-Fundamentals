# Write a function that checks if a given password is valid. Password validations are:
# •	The length should be 6 - 10 characters (inclusive)
# •	It should consists only letters and digits
# •	It should have at least 2 digits
# If a password is valid print "Password is valid".
# If it is NOT valid, for every unfulfilled rule print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"
#
# Input	            Output
# logIn	            Password must be between 6 and 10 characters
#                   Password must have at least 2 digits


def is_password_valid(password):
    has_enough_letters = False
    has_enough_digits = False
    has_only_l_and_d = True
    digit_count = 0
    if 6 <= len(password) <= 10:
        has_enough_letters = True
    else:
        print("Password must be between 6 and 10 characters")

    for each_char in password:
        # 48 - 57 - digits, 65 - 90 - capital letters, 97 -122 - lowercase letters
        if 48 <= ord(each_char) <= 57:
            digit_count += 1
        if ord(each_char) < 48 or 57 < ord(each_char) < 65 or 90 < ord(each_char) < 97 or ord(each_char) > 122:
        # if 48 <= ord(each_char) <= 57 or not 65 <= ord(each_char) <= 90 or not 97 <= ord(each_char) <= 122:
            has_only_l_and_d = False

    if not has_only_l_and_d:
        print("Password must consist only of letters and digits")

    if digit_count < 2:
        print("Password must have at least 2 digits")
    else:
        has_enough_digits = True

    if has_enough_digits and has_only_l_and_d and has_enough_letters:
        print("Password is valid")


if __name__ == "__main__":
    password_str = input()
    is_password_valid(password_str)


