class animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("some bla bla bla")

    def description(self):
        print(f"this animal is named {self.name}.")

class dog(animal):
    def __init__(self, name, breed):

    def sound(self):
        print("ham ham")


class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print()



        class cat(animal):
            def __init__(self, name, breed):
                super().__init__(name)
                self.breed = breed


            def sound(self):
                print("meow")

            def description(self):
                super().descrption()


            print(f"color: {self.color}")


animal = animal(eh more bir)
animal.sound()
animal.description()

dog = dog(name:"rex", breed:"pitbull")
dog.sound()
dog.descrition()

cat = cat(name:"aehhhh", breed:"black")
cat.sound()
cat.descrition()














