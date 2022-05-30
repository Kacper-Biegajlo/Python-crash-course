## 4-11. My Pizzas, Your Pizzas: 
# Start with your program from Exercise 4-1 (page 56). 

# Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:

# * Add a new pizza to the original list.

pizzas = ['pepperoni', 'margharita', 'vegan']
friend_pizzas = pizzas[:]

pizzas.append('Cheese')

# * Add a different pizza to the list friend_pizzas.

friend_pizzas.append('Hawaii')

# * Prove that you have two separate lists. 

# Print the message My favorite pizzas are:, 
#   and then use a for loop to print the first list. 

# Print the message My friend’s favorite pizzas are:, 
#   and then use a for loop to print the second list. 

# Make sure each new pizza is stored in the appropriate list.

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

## 4-12. More Loops: All versions of foods.py in this section have avoided 
#   using for loops when printing to save space.

#  Choose a version of foods.py, and write two for loops to 
#   print each list of foods.

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

