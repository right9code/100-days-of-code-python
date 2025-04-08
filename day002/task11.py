# Number manipulation in Python

# round Function : to round a number to closest integer...
print(round(22 / 7))

#rounding to certain number of decimals e.g. 11 digits...
print(round(22 / 7, 13))

# Flow Division: "//" , with this operation we can directly get integer value instead of float as is case with division...
print(79 // 10)
# Remember the output is 7 so it is not rounding of just providing the integer part...

# Performing chain calculation...
result = 64 / 2 # i.e.32
result /=2 # i.e. 16
result /=2  # i.e. 8

print(result)

# Another example of chain calculation...
result_pemdas = 10 + 6 # i.e. 16
result_pemdas -=4 # i.e. 12
result_pemdas *=10 #i.e 120
result_pemdas /= 10

print(result_pemdas)