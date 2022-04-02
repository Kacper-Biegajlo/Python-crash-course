## 0-5. Programming Poll: 
# 
# Write a while loop that asks people why they like programming. 
# 
# Each time someone enters a reason, add their reason to a file that stores 
#   all the responses.

filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
        file_object.write('Poll results:\n')

prompt = "\nPlease tell me your name:"
prompt += "\n(Enter 'done' when you are polling is finished.) "

while True:
    name = input(prompt)
    if name == 'done':
        break
    else:
        prompt2 = f"\nWhy do you like programming {name}?"
        reason = input(prompt2)
        with open(filename, 'a') as file_object:
            print(f"Thank you for your opinion! {name}!")
            file_object.write(f"{name}: {reason}\n")