def underweight(bmi):
    if bmi < 18.5:
        print("You are Underweight.")

def normalweight(bmi):
    if 18.5 <= bmi < 25:
        print("You are Normal weight.")

def overweight(bmi):
    if 25 <= bmi < 30:
        print("You are Overweight.")

def obese(bmi):
    if bmi >= 30:
        print("You are Obese.")

print("Welcome to BMI Calculator!")

user_weight = float(input("Enter weight in kg: "))
user_height = float(input("Enter height in meters: "))

bmi = user_weight / (user_height ** 2)
print("Your BMI is:", bmi)

# Call the functions with bmi as an argument
underweight(bmi)
normalweight(bmi)
overweight(bmi)
obese(bmi)