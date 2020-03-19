#Client name: Professor Laura Atkins
#Programmer name: Brendan Boyle
#PA Purpose: Given the user's weight and height, this program converts that to metric measurements and shows the user their Body Mass Index.
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

weightLbs = eval(input("Enter your weight in pounds:"))
heightIn = eval(input("Enter your height in inches:"))

weightKg = (weightLbs * 0.453592)
heightM = (heightIn * 0.0254)

print("Your weight in kilograms is:", weightKg)
print("Your height in meters is:", heightM)

bmi = (weightKg / (heightM**2))

print("Your BMI is:", bmi)
