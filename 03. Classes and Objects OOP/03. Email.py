# Create a class Email as described in the lab description
# You will receive some emails until you receive "Stop" (separated by single space)
# The first will be the sender, the second one – the receiver and the third one – the content
# On the final line you will be given the indices of the sent emails separated by comma and space.
# For each email print:"{sender} says to {receiver}: {content}. Sent: {is_sent}"


class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):  # we don't need to receive an attribute here
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

    def print_email(self):
        return self.sender, self.receiver, self.content


emails_list = list()

user_input = input()

while not user_input == "Stop":
    line = user_input.split(" ")
    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails_list.append(email)

    user_input = input()

indexes = input().split(", ")
for each_index in indexes:
    emails_list[int(each_index)].send()

for each_email in emails_list:
    print(each_email.get_info())
