# type FUNCTION

# Type Checking: identify the type of data with type function

name_length = len(input( "What is your name dear?\n"))
# print("Your name has " + name_length + " characters") this gives error because we can't concatenate str(string) to int(integer)

print(type(name_length))

# output: <class 'int'> ,which shows it is integer class
