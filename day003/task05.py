# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating,
# This is how you work out whether if a particular year is a leap year:
#     on every year that is divisible by 4 with no remainder
#     except every year that is evenly divisible by 100 with no remainder
#     unless the year is also divisible by 400 with no remainder

print("Welcome to LEAP YEAR DETECTOR!!")
year = int(input("PLease enter a year to check.\n"))

if year % 4 == 0:
    # if the year is divisible by 4 check further
    if year % 100 == 0:
        # if the same is also divisible by 100 check further
        if year % 400 == 0:
            # if the same year is divisible  by 400 
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is NOT a leap year.") 
    