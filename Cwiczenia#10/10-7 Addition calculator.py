## 0-7. Addition Calculator: 
# 
# Wrap your code from Exercise 10-6 in a while loop so the user can continue 
#   entering numbers even if they make a mistake and enter text instead of a 
#       number.

print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    if first_number or second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("For program to work both inputs need to be numbers only!")
    else:
        print(answer)

# So i think it is the same program as in 10-6 because I already used a loop

# I would rather have user to come back to the input where he did not put int
#   correctly but currently I dont have an idea how to do it. 

# And I made code look more neat. Pog