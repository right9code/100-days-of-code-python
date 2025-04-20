# Pizza Order Calculator

# Congratulations, you've got a job at ABHI's PIZZA PLACE! 
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): Rs. 150
# Medium pizza (M): Rs. 200
# Large pizza (L): Rs. 250
# Add pepperoni for small pizza (Y or N): +50
# Add pepperoni for medium or large pizza (Y or N): +70
# Add extra cheese for any size pizza (Y or N): +40

print("Welcome to ABHI's PIZZA PLACE!!")
size = input("What size of pizza would you like? S,M or L\n")
bill = 0 # Starting with zero is important to avoid errors
if size == "S":
    bill = 150
    print(f"That would be Rs. {bill}.")
if size == "M":
    bill = 200
    print(f"That would be Rs. {bill}.")
if size == "L":
    bill = 250
    print(f"That would be Rs. {bill}.")
# else:
    # print("Thank You for visiting...")
add_pepperoni = input("Would you like to add Pepperoni? Y or N\n")
if add_pepperoni == "Y":
    if bill == 150:
        bill += 50
        print(f"You total is now Rs. {bill}.")
    else:
        bill += 70
        print(f"Your total is now Rs. {bill}.")
else:
    print(f"Your total is still Rs. {bill}.")
extra_cheese = input("Would you like extra chesse? Y or N.\n")
if extra_cheese == "Y":
    bill += 40
    print(f"Thanks for visiting ABHI's PIZZA PLACE!!\nYour final bill is Rs. {bill}.")
else:
    print(f"Thanks for visiting ABHI's PIZZA PLACE!!\nYour final bill is Rs. {bill}.")

