## 7-5. Movie Tickets:

# A movie theater charges different ticket prices depending on a person’s age. 

# If a person is under the age of 3, the ticket is free; if they are
#   between 3 and 12, the ticket is $10; and if they are over age 12, 
#       the ticket is $15. 

# Write a loop in which you ask users their age, and then tell them 
#   the cost of their movie ticket.

prompt = "\nWelcome to our cinema! \
    Please enter your age to check the ticket price: "

age = ""

while age == "":
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        print(f"Ticket for someone who is {age} yo is free!")
    elif age >= 3 and age <= 12:
        print(f"Ticket price for someone who is {age} yo is 10$!")
    elif age > 12:
        print(f"Ticket price for someone who is {age} yo is 15$!")

