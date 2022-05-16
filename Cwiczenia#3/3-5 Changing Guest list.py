## 3-5. Changing Guest List ##

# You just heard that one of your guests can’t make the dinner, 
#   so you need to send out a new set of invitations. 

# You’ll have to think of someone else to invite.


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
print("\t")


cant_attend = 'kaczor' #remove method
Guest_list.remove(cant_attend)
print(f"{cant_attend.title()} sadly can't make it to my dinner.")
print("\t")

# pop method
Guest_list = ['kaczor', 'mc', 'vacool', 'fresh'] 
print(f"{Guest_list.pop(0).title()} sadly can't make it to my dinner.") 
print("\t")

# method with chaning one value in the list to another
Guest_list = ['kaczor', 'mc', 'vacool', 'fresh']
print(f"{Guest_list[0].title()} sadly can't make it to my dinner.")
Guest_list[0] = 'Slupek'
print("\t")

# loop that prints invitation message to each person 
# while removing them from the list 
for f in range(len(Guest_list)): 
    Dinner_Inv = f"Hello {Guest_list.pop(0).title()}\
, I would like to invite you for a dinner."
    print(Dinner_Inv)
print(Guest_list)

