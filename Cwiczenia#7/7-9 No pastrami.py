## 7-9. No Pastrami:
# 
# Using the list sandwich_orders from Exercise 7-8, 
#   make sure the sandwich 'pastrami' appears in the list at least three times.
# 
# Add code near the beginning of your program to print a message saying 
#   the deli has run out of pastrami, and then use a while loop to remove
#       all occurrences of 'pastrami' from sandwich_orders. 
# 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Egg sandwich', 'Ham sandwich', 'Grilled cheese sandwich',\
    'Seafood sandwich', 'Nutella sandwich', 'Pastrami sandwich',\
    'Pastrami sandwich', 'Pastrami sandwich']

finished_sandwiches = []

sandwich_loop_active = True

if 'Pastrami sandwich' in  sandwich_orders:
    print('Sorry, we run out of Pastrami :(\n')

while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

print("TIME TO MAKE SOME SANDWICHES!\n")

while sandwich_loop_active:
    # preparing a sandwich beep boop pap
    print("A few moments later...")
    current_sandwich = sandwich_orders.pop()
    print(f"I just prepared your {current_sandwich.lower()}!\n")
    finished_sandwiches.append(current_sandwich)

    if sandwich_orders == []:
        sandwich_loop_active = False
print("\nList of sandwiches that I already made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# quick look at list of finished sandwiches just to be sure
print('\n')
print(finished_sandwiches)
