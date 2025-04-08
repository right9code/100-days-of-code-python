# Tip Calculator

# Print welcome message for the app...
print("Welcome to Tip Calculator!!")

# Get input for total bill, percentage of tip, number of people sharing...
bill = input("What was the total bill?\nRs.")
percentage = input("How much tip would you like to give? 10, 12 or 15 percent)?\n")
people = input("How many people are splitting the bill?\n")

# Calculate total tip value...
tipvalue = float(percentage)/float(bill)*100 

# Calculate total bill after adding tip value...
total_bill = float(bill) + tipvalue

# Divide the bill among required people and round of the value to two decimal points...
share = round(total_bill / float(people),2)

# That is simple but if the value come to something like 12.20 it would ignore the zero so we need to do some formatting..
# Here 2f is no. of decimal points we want to limit the answer to
formatted_share = "{:.2f}".format(share)

# Print the result...
print(f"Each person needs to pay {formatted_share} rupees.\n")

