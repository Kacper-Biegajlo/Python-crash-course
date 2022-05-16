## 7-8. Deli: 
# Make a list called sandwich_orders and fill it with the names of 
#   various sandwiches. 
# 
# Then make an empty list called finished_sandwiches. 
#
# Loop through the list of sandwich orders and print a message 
#   for each order, such as I made your tuna sandwich. 
# 
# As each sandwich is made, move it to the list of finished sandwiches. 
# 
# After all the sandwiches have been made, print a message listing each 
#   sandwich that was made.

sandwich_orders = ['Egg sandwich', 'Ham sandwich', 'Grilled cheese sandwich',\
    'Seafood sandwich', 'Nutella sandwich']

finished_sandwiches = []

sandwich_loop_active = True

while sandwich_loop_active:
    # preparing a sandwich beep boop pap
    current_sandwich = sandwich_orders.pop()
    print(f"I just prepared your {current_sandwich.lower()}!")
    finished_sandwiches.append(current_sandwich)

    if sandwich_orders == []:
        sandwich_loop_active = False
print("\nList of sandwiches that I already made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
