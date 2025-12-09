from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class  circle(shape):
    def __init__(self,redius):
        self.redius=redius

    def area(self):
        return 3.14*slef.radius*self.redius

class Square(shape):
    def __init__(self,length):
        slef.length=length

    def area(self):
        return self.length*slef.length


circle_1=clircle(7)
print(circle_1.area())

square_1=square(10)
print(square_1.area())























