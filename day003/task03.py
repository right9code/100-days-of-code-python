# Nested "if-else" Statements:
# You put "if-else" Statements inside "if-else" Statements this is called nesting.


# "elif" STATEMENT:
# The elif keyword is pythons way of saying "else if" "if the previous conditions were not true, then try this condition".

print("Welcome to the ABHI Rollercoaster!!")
height = int(input("\nPlease input your height in cm ?\n"))

if height >= 120:
    print("\nYou can ride the Rollercoaster.")
    age = int(input("Please enter you age.\n"))
    if age <= 12:
        print("\nIt will cost you Rs.100")
    elif age < 18:
        print("It will cost you Rs. 150")
    else:
        print("It will cost you Rs. 200")
else:
    print("\nSorry, You need to grow a lil more to ride the Rollercoaster.")


