# Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
# Make a program that receives an age, and returns what they drink.
# Rules:
# Kids under 14 years old.
# Teens under 18 years old.
# Young adults under 21 years old.
# Adults above 21.
# Note: All the values except the last one are inclusive!

age = int(input())

if age <= 14:
    drink = 'toddy'
elif 14 < age <= 18:
    drink = 'coke'
elif 18 < age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f"drink {drink}")
