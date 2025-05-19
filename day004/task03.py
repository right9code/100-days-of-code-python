# Lists..

states_of_matter = ["BCE", "solid", "liquid", "plasma", "gas",] 
# making a list also make sure to add a comma in the end if you want to use reverse sorting too...

print(states_of_matter[0])
# print out the first entry from the list..

print(states_of_matter[-1])
# print out the first entry from the end ; 0 is always the anchor/ first element of list  

states_of_matter[3] = "PLASMA"
# to change a entry in the list..

states_of_matter.append("chaos")
# adding a new entry to the end of the list by using append..

print(states_of_matter)

states_of_matter.extend(["xxx", "yyy", "zzz",])

print(states_of_matter)


      