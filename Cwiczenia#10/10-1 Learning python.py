## 10-1. Learning Python: 
# 
# Open a blank file in your text editor and write a few lines summarizing what 
#   you’ve learned about Python so far. 
# 
# Start each line with the phrase In Python you can. . .. 
# 
# Save the file as learning_python.txt in the same directory as your exercises 
#   from this chapter. 
# 
# Write a program that reads the file and prints what you wrote three times. 
# 
# Print the contents once by reading in the entire file, once by looping over 
#   the file object, and once by storing the lines in a list and then working 
#       with them outside the with block.

filename = 'learning_python.txt'

print("\nPrinting using .read():")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("\nPrinting using loop:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nPrinting using list and working with them outside the block:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())