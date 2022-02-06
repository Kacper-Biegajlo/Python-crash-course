## Pizzas ##

# Think of at least three kinds of your favorite pizza. 

# Store these pizza names in a list,
#   and then use a for loop to print the name of each pizza.

print("\n"+"Pizza list:"+"\n")

pizzas = ['pepperoni', 'margharita', 'vegan']
for pizza in pizzas:
    print(f"{pizza.title()}")

# * Modify your for loop to print a sentence using the name of the pizza 
#   instead of printing just the name of the pizza. 

# For each pizza you should have one line of output containing 
#   a simple statement like I like pepperoni pizza.

print("\n"+"Pizza list:"+"\n")

pizzas = ['pepperoni', 'margharita', 'vegan']
for pizza in pizzas:
    print(f"{pizza.title()}")
    print(f"{pizza.title()} pizza can be ordered in Roma restaurant!")

# * Add a line at the end of your program, outside the for loop,
#    that states how much you like pizza. 

# The output should consist of three or more lines about the kinds of pizza you 
#   like and then an additional sentence, such as I really love pizza!

print("\n"+"Pizza list:"+"\n")

pizzas = ['pepperoni', 'margharita', 'vegan']
for pizza in pizzas:
    print(f"{pizza.title()}")
    print(f"{pizza.title()} pizza can be ordered in Roma restaurant!\n")
print("\n"+"I order pizza from Roma restaurant every week.")