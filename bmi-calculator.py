# BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("=== BMI Calculator ===")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = calculate_bmi(weight, height)
    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

if __name__ == "__main__":
    main()
