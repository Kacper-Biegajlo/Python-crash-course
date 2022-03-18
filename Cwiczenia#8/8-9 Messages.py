## 8-9. Messages: 
# 
# Make a list containing a series of short text messages. 
# 
# Pass the list to a function called show_messages(), 
#   which prints each text message.

short_messages = ["I like cats", "Kaczor is a cool guy", "Vacool is\
 ginger", "Mc will soon be a daddy"]

def show_messages(messages):
    """Print a each short message from the list."""
    print("All short messages from the list:")
    for message in messages:
        print(f"{message}.")

show_messages(short_messages)