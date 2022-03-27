## 9-15. Lottery Analysis: 
# 
# You can use a loop to see how hard it might be to win the kind of lottery you 
#   just modeled. 
# 
# Make a list or tuple called my_ticket. 
# 
# Write a loop that keeps pulling numbers until your ticket wins. 
# 
# Print a message reporting how many times the loop had to run to give you a 
#   winning ticket.

from random import choice
# since we want to sort our ticket to give better comparison we treat ints as 
#    strings in this exercise

# now for my ticket and loop that will compare 
my_ticket = ['6', '9', '6', 'A']
my_ticket.sort()
print(f"\nMy ticket is: {my_ticket}")
rolls_number = 0

lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B'\
, 'C', 'D', 'E']
win_ticket = []

while my_ticket != win_ticket:
    win_ticket = [] #reseting winning ticket list
    for number in range(4): # pulling new winning ticket from lottery
        pull = choice(lottery_list)
        win_ticket.append(pull)
    rolls_number += 1
    win_ticket.sort()
    
print(f"\nIt took {rolls_number} lotteries for my ticket to win.")
if my_ticket == win_ticket:
    print("Congratulations to myself! I WON POG!")

# Some parts of this program may be removed or changed for sure lol