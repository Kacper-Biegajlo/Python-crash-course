## 3-6. More Guests ##

# You just found a bigger dinner table, so now more space is available. 
#   Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print() call to the end of your program informing people 
    # that you found a bigger dinner table.

# - Use insert() to add one new guest to the beginning of your list.
# - Use insert() to add one new guest to the middle of your list.
# - Use append() to add one new guest to the end of your list.
# - Print a new set of invitation messages, one for each person in your list.


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