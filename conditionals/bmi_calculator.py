weight = float(input("What's your weight (kg)? "))
height = float(input("What's your height (cm)? "))
bmi = weight / ((height/100)**2)

if bmi < 18.5:
  print(f"BMI: {bmi:.2f} - Underweight.")
elif bmi < 25:
  print(f"BMI: {bmi:.2f} - Normal.")
elif bmi < 30:
  print(f"BMI: {bmi:.2f} - Overweight.")
else:
  print(f"BMI: {bmi:.2f} - Obese.")
