# Test class for pets.


class Pet:
    species = "dog"

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def species_identifier(self, species):
        self.species = species


first_pet = Pet("Lassie", 5)
second_pet = Pet("Garfield", 4)

print(first_pet.species)  # dog
print(second_pet.species)  # dog
second_pet.species_identifier("cat")
print(second_pet.species)  # cat

