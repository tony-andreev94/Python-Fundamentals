# Create an example of a class "Person" that has, first name, last name and age,
# age should be optional and have default value of 0.


class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def age_modifier(self, age):
        self.age += 1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# Output tests
user1 = Person("Tony", "Andreev", 26)
print(user1.first_name)  # Tony
print(user1.get_full_name())  # Tony Andreev
print(user1.age)  # 26

# Attribute modification tests
user1.age += 1  # bad practice, we should define another method to modify attributes
print(user1.age)  # 27

user2 = Person("Max", "Mustermann")
print(user2.age)  # 0
user2.age_modifier(user2.age)
print(user2.age)  # 1
