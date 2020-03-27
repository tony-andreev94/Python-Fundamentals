class Person:
    def __init__(self, name):
        self.name = name


class Email:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender.name} says to {self.recipient.name}: {self.content}. Sent: {self.is_sent}"


class Mailbox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_email(self, indexes):
        for i in indexes:
            self.emails[i].send()
