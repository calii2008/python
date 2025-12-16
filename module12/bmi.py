# Funksioni për llogaritjen e BMI-së
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Funksioni për të përcaktuar statusin e BMI-së
def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Përdoruesi jep informacionin e tij
def main():
    print("Mirësevini në programin për llogaritjen e BMI-së!")

    # Marrja e të dhënave nga përdoruesi
    name = input("Shkruani emrin tuaj: ")
    age = int(input("Shkruani moshën tuaj: "))
    weight = float(input("Shkruani peshën tuaj në kilogramë (kg): "))
    height = float(input("Shkruani lartësinë tuaj në metra (m): "))

    # Llogaritja e BMI-së
    bmi = calculate_bmi(weight, height)

    # Përcaktimi i statusit të BMI-së
    status = get_bmi_status(bmi)

    # Shfaqja e informacionit për përdoruesin
    print("\n--- Informacioni i përdoruesit ---")
    print(f"Emri: {name}")
    print(f"Mosha: {age} vjeç")
    print(f"Pesha: {weight} kg")
    print(f"Lartësia: {height} m")
    print(f"Indeksi i Masës Trupore (BMI): {bmi:.2f}")
    print(f"Statusi i BMI-së: {status}")


# Ekzekutimi i programit
if __name__ == "__main__":
    main()
