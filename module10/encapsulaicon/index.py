class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

    student1=student("daris",15)

    print("name:",student1.get_name())

    student1.set_name("blin")
    print("name:",student.get_name())

    print("age:",student.get_age())
    student1.set_age(16)
    print("age:",student1.get.age())


















