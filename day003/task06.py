# Multiple If Statements in Succession




print("Welcome to the ABHI Rollercoaster!!")
height = int(input("\nPlease input your height in cm ?\n"))

if height >= 120:
    print("\nYou can ride the Rollercoaster.")
    age = int(input("Please enter you age.\n"))
    if age <= 12:
        bill = 100
        print("\nChild ticket costs Rs.100")
    elif age < 18:
        bill = 150
        print("Youth ticket costs Rs. 150")
    else:
        bill = 200
        print("\nAdult ticket costs Rs. 200")
    photo = input("Do you want a photo? Replay with Y or N.\n")
    if photo == "Y":
        # add Rs. 50 to the bill; "+=" is used to add value to the same variable and save as same variable
        bill += 50
    print(f"Your total bill is Rs. {bill}.")
else:
    print("\nSorry, You need to grow a lil more to ride the Rollercoaster.")


