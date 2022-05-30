## 4-13. Buffet: A buffet-style restaurant offers only five basic foods. 
# Think of five simple foods, and store them in a tuple.

menu = ('spaghetti', 'burger', 'pizza', 'meat balls', 'steak')

# * Use a for loop to print each food the restaurant offers.

print('\nOur restaurnt offers:')
for food in menu:
    print(food.title())

# * Try to modify one of the items, and make sure that Python rejects the change.

# menu[0] = 'lasanghe' stops the program with an error

# * The restaurant changes its menu, 
#       replacing two of the items with different foods. 

# Add a line that rewrites the tuple, 
#   and then use a for loop to print each of the items on the revised menu.

menu = ('lasanghe', 'burger', 'fish&chips', 'meant balls', 'steak')
print('\nIn our new menu we offer:')
for food in menu:
    print(food.title())
