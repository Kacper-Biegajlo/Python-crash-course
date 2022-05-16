## 7-6. Three Exits: 

# Write different versions of either Exercise 7-4 or Exercise 7-5 
#   that do each of the following at least once:

# - Use a conditional test in the while statement to stop the loop. 
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enters a 'quit' value.


# VERSION WITH THE 'BREAK'
prompt = "\nPlease tell me what toppings would you like on your pizza:"
prompt += "\n(Enter 'done' when you are finished.) "

while True:
    topping = input(prompt)
    if topping == 'done':
        print('Your pizza is done')
        break
    else:
        print(f"{topping.title()} has been added to your pizza!")

# VERSION WITH CODITIONAL TEST

prompt = "\nPlease tell me what toppings would you like on your pizza:"
prompt += "\n(Enter 'done' when you are finished.) "

topping = ""

while topping != 'done':
    topping = input(prompt)
    print(f"{topping.title()} has been added to your pizza!")

    if topping == 'done':
        print('Your pizza is done')

# VERSION WITH ACTIVE VARIABLE 

prompt = "\nPlease tell me what toppings would you like on your pizza:"
prompt += "\n(Enter 'done' when you are finished.) "

active = True

while active == True:
    topping = input(prompt)
    if topping == 'done':
        print('Your pizza is done')
        active = False 
    else:
        print(f"{topping.title()} has been added to your pizza!")