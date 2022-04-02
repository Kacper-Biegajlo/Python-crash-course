## 10-4. Guest Book: 
# 
# Write a while loop that prompts users for their name. 
# 
# When they enter their name, print a greeting to the screen and add a line 
#   recording their visit in a file called guest_book.txt. 
# 
# Make sure each entry appears on a new line in the file.

filename = 'guest_list.txt'

with open(filename, 'w') as file_object:
        file_object.write('Guest list:\n')

prompt = "\nPlease tell me your name:"
prompt += "\n(Enter 'done' when you are finished.) "

while True:
    name = input(prompt)
    if name == 'done':
        break
    else:
        with open(filename, 'a') as file_object:
            print(f"Welcome to our Gacchi Club {name}!")
            file_object.write(f"- {name}\n")