class Dog:

    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes a sound:wolf!")


class Cat:

    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound:meow!")


class Bird:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound:ciu ciu!")

dog=Dog("buddy")
cat=Cat("whiskurs")
bird=Bird("tweetie")

for animal in (dog,cat,bird):
    animal.sound()

























