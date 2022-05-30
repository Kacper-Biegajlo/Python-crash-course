## 3-7. Shrinking Guest List ##

# You just found out that your new dinner table won’t arrive 
#   in time for the dinner, and you have space for only two guests.

# - Start with your program from Exercise 3-6. Add a new line that prints 
#       a message saying that you can invite only two people for dinner.

# -  Use pop() to remove guests from your list one at a time
#       until only two names remain in your list. 

# Each time you pop a name from your list, print a message to that person
#    letting them know you’re sorry you can’t invite them to dinner.

# - Print a message to each of the two people still on your list, 
#       letting them know they’re still invited.

# - Use del to remove the last two names from your list,
#        so you have an empty list. 

# Print your list to make sure you actually 
#   have an empty list at the end of your program.

Guest_list = ['kaczor', 'mc', 'vacool', 'fresh'] 
print("\t")

# loop that prints invitation message to each person 
for f in range(len(Guest_list)): 
    Dinner_Inv = f"Hello {Guest_list[f].title()}\
, I would like to invite you for a dinner." 
    print(Dinner_Inv)
print("\t")

print("Guys I found bigger table! I will invite few more pops.")
print("\t")

Guest_list.insert(0, 'olsen')
Guest_list.insert(3, 'bobek')
Guest_list.append('pixel')

# loop that prints invitation message to each person 
for f in range(len(Guest_list)): 
    Dinner_Inv = f"Hello {Guest_list[f].title()}\
, I would like to invite you for a dinner." 
    print(Dinner_Inv)
print("\t")

print(Guest_list)
print("\t")

print("Sorry guys, I can only invite 2 people. :(")
print("\t")

# loop that prints invitation cancel message to 5 first people
for f in range(5): 
    Dinner_cancel = f"Hello {Guest_list.pop(0).title()}\
, sorry but I have to cancel your dinner inviation." 
    print(Dinner_cancel)
print("\t")

# loop that prints invitation message to 2 people left
for f in range(len(Guest_list)): 
    Dinner_Inv_fin = f"Hello {Guest_list.pop(0).title()}\
, I would like to still invite you for a dinner." 
    print(Dinner_Inv_fin)
print("\t")

print(Guest_list)
print("\t")