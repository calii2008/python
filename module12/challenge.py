# Klasa bazë
class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    # Metodë që do të mbishkruhet (polymorphism)
    def bmi_status(self):
        pass

    def display_info(self):
        bmi = self.calculate_bmi()
        print("\n--- Të dhënat e personit ---")
        print(f"Emri: {self.name}")
        print(f"Mosha: {self.age}")
        print(f"Pesha: {self.weight} kg")
        print(f"Gjatësia: {self.height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Statusi: {self.bmi_status()}")


# Klasa për të rritur
class Adult(Person):
    def bmi_status(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# Klasa për fëmijë (shembull i polymorphism)
class Child(Person):
    def bmi_status(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        else:
            return "Overweight"


# Programi kryesor
def main():
    print("BMI Calculator (OOP & Polymorphism)")

    name = input("Shkruani emrin: ")
    age = int(input("Shkruani moshën: "))
    weight = float(input("Shkruani peshën (kg): "))
    height = float(input("Shkruani gjatësinë (m): "))

    # Polymorphism në veprim
    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    person.display_info()


if __name__ == "__main__":
    main()
0