## 4-10. Slices: 

# Using one of the programs you wrote in this chapter, 
#   add several lines to the end of the program that do the following:

# * Print the message The first three items in the list are:. 
#       Then use a slice to print the first three items from that program’s list.

print("\n"+"Multiples of 3 from 3 to 30:")

for value in range(1,11):
    print(value*3)

print("\n"+"First three multiples of 3 from previous list are:")

multiplies = [value*3 for value in range(1,11)]

# slice of first three multiplies of number 3
print(multiplies[0:3]) 

# * Print the message Three items from the middle of the list are:. 
#       Use a slice to print three items from the middle of the list.

print("\n"+"Multiples of 3 from 3 to 30 in form of a list:")
print(multiplies)

# change 3 middle items to 4 to make it look more even
print("\n"+"Middle 4 multiplies of 3 from 3 to 30:") 
print(multiplies[3:7])

# * Print the message The last three items in the list are:.
#        Use a slice to print the last three items in the list.

print("\n"+"Last 3 multiplies of 3 from 3 to 30:")
print(multiplies[-3:])