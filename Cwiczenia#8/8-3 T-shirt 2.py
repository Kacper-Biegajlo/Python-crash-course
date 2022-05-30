## 8-3. T-Shirt: 
# 
# Write a function called make_shirt() that accepts a size and the text of 
#   a message that should be printed on the shirt. 
# 
# The function should print a sentence summarizing the size of the 
#   shirt and the message printed on it.
# 
# Call the function once using positional arguments to make a shirt. 
# 
# Call the function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_message):
    print(f"<<<Printing {shirt_size} shirt with message:'{shirt_message}'.>>>")

make_shirt('medium', 'I have huge cock')

make_shirt(shirt_size="large", shirt_message="My cock ain't that big")