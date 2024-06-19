w=float(input("Enter your weight in kg"))
h=float(input("Enter your Hight in meter"))

bmi= w/(h)**2

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")