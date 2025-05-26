# random module: is used to generate pseudo-random numbers in Python..

import random
# import the module to use..

random_integer = random.randint(1, 10)
# create a variable that selects random integer FROM 1 to 10

print(random_integer)
# print the output..

random_float = random.random()
# create a variable that select a float  (by default its BETWEEN 0 and 1)..

exp_random_float = random_float * 7
# expanding the range of float BETWEEN 0 and 7 by multiplying by 7

#print(random_float) 

print(exp_random_float)
