## 9-14. Lottery: 
# 
# Make a list or tuple containing a series of 10 numbers and five letters. 
# 
# Randomly select four numbers or letters from the list and print a message 
#   saying that any ticket matching these four numbers or letters wins a prize.

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
win_list= []

from random import choice

for number in range(4):
    pull = choice(lottery_list)
    win_list.append(pull)

print(f"Winning ticket is: {win_list}.")