# Jenny studies programming with python and wants to create a program that greets a user when he/she gives his/her name.
# Jenny however is in love with Johnny, and would like to greet him differently. Can you help her?
# Input	        Output
# Peter	        Hello, Peter!
# Amy	        Hello, Amy!
# Johnny	    Hello, my love!

user_name = input()

if user_name == 'Johnny':
    print(f"Hello, my love!")
else:
    print(f"Hello, {user_name}!")
