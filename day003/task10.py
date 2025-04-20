# LOVE CALCULATOR PROGRAM

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 1O or greater than 90, the message should be:
# "your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y* , you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z* . "
# e.g.
# name1 = "Angela Yu"
# name2 — "Jack Bauer"

print("Welcome to LOVE CALCULATOR!!")

# take name input with name1 and name 2..
name1 = input("Enter your name?\n")
name2 = input("Enter your partner's name?\n")

# combine the names..
combined_name = name1 + name2

# use lower method to convert combined_name to lowercase..
lower_names = combined_name.lower()

# use count method to count the occurrence of of a specific letter in the combined string..
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

# add all the counts with concatenation for the first digit..
first_digit = t + r + u + e

# similarly use count method to count the occurrence of of a specific letter in the combined string..
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

# add all the counts with concatenation for the second digit..
second_digit = l + o + v + e

# change the counts to score as integer with concatenation of strings then convert to integers..
score = int(str(first_digit) + str(second_digit))

# print response based on conditions of program..
if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

