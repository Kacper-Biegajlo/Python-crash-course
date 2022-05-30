## 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether 
#   the number is a multiple of 10 or not.

number = input("Please choose a number: ")
number = int(number)

if number % 10 == 0:
    print("Your nuber is a multiple of 10! Pog")
else:
    print("Unfortunatelly your number is not a multiple of 10. Sadge")