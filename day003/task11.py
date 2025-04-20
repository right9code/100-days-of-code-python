# PROJECT TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
      ''')
# we used three single quotes to string the multiblock ascii art






print("Welcome to the TREASURE ISLAND!!\nYour mission is to find treasure.\n")

direction = input('You\'re at a crossroad. Where do you wanna go? "left" or "right".\n').lower()
# we used backslash "\" to make the code skip to identify single quotes in you're as a string closing argument and just treat is as string..
# also we used .lower to make the input lowercase..
if direction == "left":
    transport = input('You have reached the LAKE. What do you wish to do? "swim" or "wait".\n').lower()
    if transport == "wait":
        door = input('You took the boat and reached the CASTLE.Which door do you want to open? "red", "yellow" or "blue".\n').lower()
        if door == "red":
            print("Burned by fire.Game Over!!\n")
        elif door == "yellow":
            print("Congratulations!! You have found the Treasure. YOU WIN!!\n")
        elif door == "blue":
            print("Eaten by Beasts.Game Over!!\n")
        else:
            print("You choose the door that doesn't exist.Game Over!!\n")
    if transport == "swim":
        print("Attacked by Trout.Game Over!!\n")
    else:
        print("You choose the method that doesn't exist.Game Over!!\n")
if direction == "right":
    print("Fell into a hole.Game Over!!\n")
else:
    print("Direction option doesnot exist.Game Over!!")

