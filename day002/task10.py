# BMI Calculator Coding Exercise

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weight the
# same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Note: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.

# Self note people in India measure their height mostly in feet sop lets make a BMI Calculator that takes it in account.


# BMI CALCULATOR

# Get the input values

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

# Print the result
print("Your BMI is " + bmi_str + ".")



