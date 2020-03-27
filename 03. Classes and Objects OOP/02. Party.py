# Create a class Party that only has an attribute called people
# The __init__ method should not accept any parameters
# You will be given names of people (on separate lines) until you receive the command "End"
# Print 2 lines:
#   "Going: " + all the people separated by comma and space
#   "Total: {total_people_going}"


class Party:
    def __init__(self):
        self.guest_list = []

    def add_guest(self, person_name):
        self.guest_list.append(person_name)

    def get_summary(self): # alternative way to have a method to print the results 
        guest_names = ', '.join([guest.name for guest in self.guest_list])
        return f"Going: {guest_names}\nTotal:{len(self.guest_list)}"


event_1 = Party()
command = input()
while not command == "End":
    #event_1.guest_list.append(command)
    event_1.add_guest(command)
    command = input()


# Printing output
print(f"Going: {', '.join(event_1.guest_list)}")
print(f"Total: {len(event_1.guest_list)}")
