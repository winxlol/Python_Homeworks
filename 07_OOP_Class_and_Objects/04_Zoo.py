class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def get_animals_count(self):
        return self.__animals

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)

        self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.zoo_name}: {", ".join(self.mammals)}'
        elif species == "fish":
            return f'Fishes in {self.zoo_name}: {", ".join(self.fishes)}'
        elif species == "bird":
            return f'Birds in {self.zoo_name}: {", ".join(self.birds)}'


zoo_name = input()
number = int(input())
my_zoo = Zoo(zoo_name)

for num in range(number):
    species, animal_name = input().split()

    my_zoo.add_animal(species, animal_name)

given_species = input()
print(my_zoo.get_info(given_species))
print(f"Total animals: {my_zoo.get_animals_count()}")



