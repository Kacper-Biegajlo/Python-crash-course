## 7-2. Restaurant Seating: 
# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message 
#   saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

seat_number = input("How many seats do you want to reserve? ")
seat_number = int(seat_number)

if seat_number > 8:
    print("\nIm sorry but you will have to wait for a table.")
else:
    print("Your table is ready.")
