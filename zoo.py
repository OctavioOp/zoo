import animal


class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name = zoo_name

    def add_Flying_animal(self, name, age, can_dive):
        self.animals.append(animal.FlyingAnimal(name, age,can_dive=can_dive))

    def add_Mammal_animal(self, name, age):
        self.animals.append(animal.MammalsAnimal(name, age))

    def add_Sea_animal(self, name, age,velocity):
        self.animals.append(animal.SeaAnimal(name, age,velocity=velocity))

    def print_info_zoo(self):
        print(f'-'*20,{self.name},'-'*20)
        for animal in self.animals:
            animal.show_status()


zoo1 = Zoo("The trash's park")
zoo1.add_Flying_animal('The super Raccoon',15,True)
print(zoo1.print_info_zoo())
