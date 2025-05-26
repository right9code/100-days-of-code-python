
# Banker Roulette: Who will pay the bill?


# Instructions:

# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# NOTE: In this exercise, you are working collaboratively withanother programmer. 
# They already dealt with input () and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.

# The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. 
# For their code to work correctly, you must enter all the names in the input area followed by comma then space. 
# e.g. name, name, name

# You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).

# Assume that names works like this:

# input area: x, y, z,

# names = ["x", "y", "z"]

# Example Input

# Angela, Ben, Jenny, Michael, Chloe

# Note: notice that there is a space between the comma and the next name.

# Example Output

# Michael is going to buy the meal today!

# Option 1
# import random
# friends = ["Manish", "Sachin", "Rakesh", "Karan", "Diksha"]
# print(random.choice(friends))


# Option 2
import random
# import random module..

friends = "Manish, Sachin, Rakesh, Karan, Diksha"
# list of choices as a string..

names = friends.split(", ")
# splits the string into a list of names..

num_items = len(names)
# number of items in the list..

random_select = random.randint(0, num_items -1)
# random select a random integer number from 0 to last no( which is "num_list - 1" i.e. 5-1 = 4; place value of last item)..

print(names[random_select])
# print from the list friends the item at the number random_select..






