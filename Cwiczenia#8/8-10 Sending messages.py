## 8-10. Sending Messages: 
# 
# Start with a copy of your program from Exercise 8-9. 
# 
# Write a function called send_messages() that prints each text message and 
#   moves each message to a new list called sent_messages as it’s printed. 
# 
# After calling the function, print both of your lists to make 
#   sure the messages were moved correctly.

short_messages = ["I like cats", "Kaczor is a cool guy", "Vacool is\
 ginger", "Mc will soon be a daddy"]

sent_messages = []

def show_messages(messages):
    """Print a each short message from the list."""
    print("All short messages from the list:")
    for message in messages:
        print(f"{message}.")

def send_messages(short_messages, sent_messages):
    """Print each short message and move it to sent_messages"""
    while short_messages:
        current_message = short_messages.pop()
        print(f"Now processing message: '{current_message}.'")
        sent_messages.append(current_message)

# function to print and move messages from one list to another
send_messages(short_messages, sent_messages)
print("\n")

# function to print messages in list called short_messages
show_messages(short_messages) 
print("\n")

# function to show messages in list called sent_messages
show_messages(sent_messages)

