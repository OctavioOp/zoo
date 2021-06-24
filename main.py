import zoo
import animal
# Menu
desition = 0
yourZoo = zoo.Zoo('yourZoo')
name = ''
age = 0
velocity = 0
subDesition = 0
dive = False
while True:
    print("Welcome to your Zoo!!")
    print("Please select an option: ")
    print("1.- Add a new animal a Flying animal")
    print("2.- Add a new animal a Mammal animal")
    print("3.- Add a new animal a Sea animal")
    print("4.- Show All animals")
    print("5.- feed an animal")
    print("6.- Exit")
    desition = round(int(input(": ")))

    if desition == 1:
        print("Create your new Flying animal!!:")
        print("Insert its name: ")
        name = input()
        print("Insert its age: ")
        age = input()
        print("Can swim?: please insert 1 for yes or 2 for no")
        subdesition = input()
        if subDesition == 1:
            dive = True
        elif subDesition == 2:
            dive = False
        yourZoo.add_Flying_animal(name, age, dive)
        print('animal added!')

    elif desition == 2:
        print("Create your new Mammal animal!!:")
        print("Insert its name: ")
        name = input()
        print("Insert its age: ")
        age = input()
        yourZoo.add_Mammal_animal(name, age)
        print('animal added!')

    elif desition == 3:
        print("Create your new sea animal!!:")
        print("Insert its name: ")
        name = input()
        print("Insert its age: ")
        age = input()
        print("Insert its velocity(km/h): ")
        velocity = input()
        yourZoo.add_Sea_animal(name, age, velocity)
        print('animal added!')

    elif desition == 4:
        print('-'*20, 'your animals', '-'*20)
        yourZoo.print_info_zoo()
        print('-'*50)

    elif desition == 5:
        print('-'*10, 'Feeding your animal', '-'*10)
        name = input('Write the name of an animal to feed it (only created): ')
        for animal in yourZoo.animals:
            if name == animal.name:
                print('Would you like to feed it? 1-yes/2-no')
                subDesition = round(int(input()))
                if subDesition == 1:
                    print('Animal fed')
                    animal.eating(True)
                elif subDesition == 2:
                    animal.eating(False)

    elif desition == 6:
        print('Good bye, all your animals gonna disapear!')
        break
