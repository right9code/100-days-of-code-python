# Life In Week Coding Exercise

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Take current age input...
age = input("What is your current age?\n")

# Subtract current age from expected age (90) to get remaining age...
rem_age = 90 - int(age)

# Calculate weeks in remaining age...
rem_weeks = rem_age * 52

# Print the result...
print(f"You have {rem_weeks} weeks left.\n")
