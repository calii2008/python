class student:
    def __init__(self,name,age):
        slef.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age


student1=studnet("daris", 15)

print("name:"student1.name)
student1.name="blin"
print("name:", student1.name)



















