# Data Type Coding Exercise

# Write a program that adds the digits in a 2 digit number. e.g. if the
# input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line I. Your program should
# work for different inputs. e.g. any two-digit number.

# Get input of required number...
two_digit_no = input("Please input a two digit number?\n")

# Get the first digit of the number...
int1 = int(two_digit_no[0])

# Get the second digit of the number...
int2 = int(two_digit_no[1])

# Print the result of sum of the two digits...
print(int1 + int2)
