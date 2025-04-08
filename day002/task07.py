# Type Conversion/Type Casting: changing a peice of data from one data type to another

# Changing int data type into string
name_length = len(input("What is your name dear?\n"))
# print("Your name has " + name_length + " characters") this gives error because we can't concatenate str(string) to int(integer)

new_name_length = str(name_length)

# now it has become a string...

print(type(new_name_length))

# Now it does not gives error...

print("Your name has " + new_name_length + " characters")

# Similarly we can convert using data type into:
# String with:  str()
# Integer with: int()
# Float with:   float()
# Boolean with: bool()
