class Party:
    def __init__(self, name):
        self.people = []
        self.name = name

    def add_people(self, name):
        self.people.append(self.name)


while True:
    names = input()
    party = Party(names)

    if names == "End":
        break

    party.add_people(names)

print(f'Going: {", ".join(party.people)}')
