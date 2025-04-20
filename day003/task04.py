# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 14.5 they are underweight.
# Equal to or over 18.5 but below 25 they have a normal weight.
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

weight = input("What is your weight in kilograms?\n")
feet = input("What is your height in feet? Don't add any additional inches yet.\n")
inches = input("And how many additional inches are there? (Enter 0 if none)\n")

# Convert input values to integers.

weight_as_int = int(weight)
feet_as_int = int(feet)
inches_as_int = int(inches)

# Convert feet into inches.

feet_into_inches = int(feet_as_int * 12)

# Calculate total height in inches

total_inches = int(feet_into_inches + inches_as_int)

# Convert height from inches to meter by multiplying by 0.0254

height_in_meters = total_inches * 0.0254

#Calculate BMI with the formula bmi is weight in kilograms divided by sqare of height in meters.
bmi = weight_as_int/height_in_meters**2

# Convert BMI into integer : 
# bmi_int = int(bmi)

# I used round function which i learned in next lesson to get more accurate output
bmi_int = round(bmi)

# Convert BMI integer into string
bmi_str = str(bmi_int)


if bmi_int < 14.5:
    print(f"Your BMI is {bmi_int} and you are UNDERWEIGHT.")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_str} and you a NORMAL weight.")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_str} and you are slightly OVERWEIGHT.")
elif bmi_int < 35:
    print(f"Your BMI is {bmi_str} and you are OBESE.")
else:
    print(f"Your BMI is {bmi_str} and you are clinically OBESE.")
