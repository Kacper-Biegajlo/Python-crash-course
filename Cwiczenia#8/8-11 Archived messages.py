## 8-11. Archived Messages: 
# 
# Start with your work from Exercise 8-10. 
# 
# Call the function send_messages() with a copy of the list of messages. 
# 
# After calling the function, print both of your lists to show that 
#   the original list has retained its messages.


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

# function to print and move messages from copy of one list to another
send_messages(short_messages[:], sent_messages)
print("\n")

# function to print messages in list called short_messages
show_messages(short_messages) 
print("\n")

# function to show messages in list called sent_messages
show_messages(sent_messages)