class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def names_of_attendees(self):
        return f"Going: {', '.join(person.name for person in self.people)}"

    def number_of_guests(self):
        return f"Total: {len(self.people)}"


party = Party()
while True:
    command = input()

    if command == "End":
        break

    name = command
    person = Person(name)
    party.invite(person)

print(party.names_of_attendees())
print(party.number_of_guests())