## 3-4. Guest List ##

# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.



Guest_list = ['kaczor', 'mc', 'vacool', 'fresh']

# loop that prints invitation message to each person 
# while removing them from the list # len(Guest_list)
# uses number of values in the list
for f in range(len(Guest_list)): 
    Dinner_Inv = f"Hello {Guest_list.pop(0).title()}\
, I would like to invite you for a dinner."
    print(Dinner_Inv)

print(Guest_list)



# standard version without the loop
Guest_list = ['kaczor', 'mc', 'vacool', 'fresh'] 

Dinner_Inv = f"Hello {Guest_list[0].title()}\
, I would like to invite you for a dinner."
print(Dinner_Inv)

Dinner_Inv = f"Hello {Guest_list[1].title()}\
, I would like to invite you for a dinner."
print(Dinner_Inv)

Dinner_Inv = f"Hello {Guest_list[2].title()}\
, I would like to invite you for a dinner."
print(Dinner_Inv)

Dinner_Inv = f"Hello {Guest_list[3].title()}\
, I would like to invite you for a dinner."
print(Dinner_Inv)

print(Guest_list)