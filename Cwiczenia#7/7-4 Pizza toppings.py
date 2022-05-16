## 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of pizza toppings 
#   until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll 
#   add that topping to their pizza.

prompt = "\nPlease tell me what toppings would you like on your pizza:"
prompt += "\n(Enter 'done' when you are finished.) "

while True:
    topping = input(prompt)
    if topping == 'done':
        break
    else:
        print(f"{topping.title()} has been added to your pizza!")

