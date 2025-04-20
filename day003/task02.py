# "modulo" OPERATOR
# The "modulo" is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# Instructions
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 + 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 + 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The "modulo" is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# - 3 with no remainder.
# therefore.
# 2 x 2 + 1, remainder is 1.
# 5
# therefore. 5 % 2 = 1
# - 3 x 4 + 2, remainder is 2.
# therefore.
# Warning: your output should match the Example Output format exactly, even the positions of the commas and full stops.

print("Welcome to the ODD/EVEN Number Checker!!")
number = int(input("Please enter a desired number to check.\n"))
if number % 2 == 0: 
# This == checks the value to be.
   print("This number is EVEN.")
else:
   print("This number is ODD.")

