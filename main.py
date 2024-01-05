


# BMI Calculator
# Hint, weight / height ** 2

print("Welcome to the Body Mass Index Calculator (BMI)")


height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Type conversion

con_height = float(height)
con_weight = int(weight)

bmi_calculator = con_weight / con_height ** 2

con_bmi_calculator = int(bmi_calculator)

if con_bmi_calculator <= 35:
    if con_bmi_calculator <= 18.5:
        print(f"Your BMI is {con_bmi_calculator}, you are underweight.")
    elif con_bmi_calculator <= 25:
        print(f"Your BMI is {con_bmi_calculator}, you have a normal weight.")
    elif con_bmi_calculator <= 30:
        print(f"Your BMI is {con_bmi_calculator}, you are slightly overweight.")
    else:
        print(f"Your BMI is {con_bmi_calculator}, you are obese.")
else:
    print(f"Your BMI is {con_bmi_calculator}, you are clinically obese.")

#  2.0 Version





