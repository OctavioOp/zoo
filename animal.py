class Animal:
    def __init__(self, name, age, lvl_health = 50, happpiness = 50) -> None:
        self.name = name
        self.age = age
        self.lvl_health = lvl_health
        self.happiness = happpiness

    def show_status(self):
        print(
            f'the animal called {self.name}, health: {self.lvl_health}, happyness: {self.happiness}')

    def eating(self, food): 
        if food == True:
            self.lvl_health += 10
            self.happiness += 10
        else:
            print('It will die of hunger')
            self.lvl_health -= 10
            self.happiness -= 10
        return self


class FlyingAnimal(Animal):
    def __init__(self, name, age, lvl_health=30, happpiness=30, can_dive=False) -> None:
        super().__init__(name, age, lvl_health, happpiness)
        self.can_dive = can_dive

    def eating(self, food):
        if food == True:
            self.lvl_health += 30
            self.happiness += 30
        else:
            print('It will die of hunger')
            self.lvl_health -= 10
            self.happiness -= 10
        return self


class MammalsAnimal(Animal):
    def __init__(self, name, age, lvl_health=80, happpiness=80) -> None:
        super().__init__(name, age, lvl_health, happpiness)

    def eating(self, food):
        if food == True:
            self.lvl_health += 5
            self.happiness += 5
        else:
            print('It will die of hunger')
            self.lvl_health -= 10
            self.happiness -= 10
        return self

    def is_Hunter(self, hunter):
        if hunter == True:
            print(f'{self.name} hunt his own food')
        else:
            print(f'{self.name} eat grass/vegetables or dead food')


class SeaAnimal(Animal):
    def __init__(self, name, age, lvl_health=5, happpiness=5, velocity = 30) -> None:
        super().__init__(name, age, lvl_health, happpiness)
        self.velocity = velocity

    def eating(self, food):
        if food == True:
            self.lvl_health += 45
            self.happiness += 45
        else:
            print('It will die of hunger')
            self.lvl_health -= 10
            self.happiness -= 10
        return self
