## 10-9. Silent Cats and Dogs: 
# 
# Modify your except block in Exercise 10-8 to fail silently if either file is 
#   missing.

def print_content(filename):
    """Print contents of text files"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.rstrip())

filenames = ('dogs.txt', 'cats.txt')
for filename in filenames:
    print_content(filename)