class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_box = []

while True:
    data = input()
    if data == "Stop":
        break

    sender, receiver, content = data.split()
    my_email = Email(sender, receiver, content)

    email_box.append(my_email)


indices = [int(el) for el in input().split(", ")]

for index in indices:
    email_box[index].send()

for email in email_box:
    print(email.get_info())