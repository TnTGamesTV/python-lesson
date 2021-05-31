class Tier:

    def __init__(self, name, type):
        self.name = name;
        self.type = type;

    def gib_name(self):
        return self.name;

    def gib_gattung(self):
        return self.type;

animals = [];

name = input("Name: ");

while name != '':
    type = input("Gattung: ");

    animal = Tier(name, type);

    animals.append(animal);

    name = input("Name: ");

for animal in animals:
    print("{} ist ein(e) {}".format(animal.gib_name(), animal.gib_gattung()));