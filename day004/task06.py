# List and IndexError Quiz:
    
# Question 1: 
# Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0][1])
# What will be printed?

    
# Ans: It will print "Nectarines"
# print(dirty_dozen[0][1])
# first it points to the '0' item in dirty_dozen list which is fruits which itself is a list then it points to '1' item in '0' list (fruits) i.e. Nectarines..


# Question 2: 
# Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# What do you think will be printed?


# Ans: ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Melons', 'Lemons']
# fruits[-1] = "Melons"
# last entry "Pears" is replaced by "Melons"..
# fruits.append("Lemons")
# a new entry at the end as "Lemons"..


# Question 3:
# Given the following list:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# Which line of code will give you "Apples"?


# Ans: print(fruits[2]) or print(fruits[-5])


