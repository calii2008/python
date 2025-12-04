import math

class shape:
    def area(self):
        pass

class circle(shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius * 2


class Ractangle(shape):

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self*height

circle=circle(5)
rectangle=Rectangle(4,6)

print(circle.area())
print(rectangle.area())
















