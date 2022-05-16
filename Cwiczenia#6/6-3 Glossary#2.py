## 6-4. Glossary 2: 
# Now that you know how to loop through a dictionary, 
#   clean up the code from Exercise 6-3 (page 99) by replacing your series of
#       print() calls with a loop that runs through the dictionary’s 
#           keys and values. 
# 
# When you’re sure that your loop works, add five more 
#    Python terms to your glossary. When you run your program again, 
#       these new words and meanings should automatically be included 
#           in the output.

# Already did that 5head but added some more examples from glossary I found

nerd_words = {
    'for': 'used to make a loop.',
    'print': 'used to display something.',
    'elif': 'something I always misspell.',
    'slice': 'preferably of pizza but also as a part of list.',
    'len': 'used to return the number of items in an object.',
    'class': 'a template for creating user-defined objects.',
    'importer': 'an object that both finds and loads a module;\
 both a finder and loader object.',
    'list': 'a built-in Python sequence.',
    'loader': 'an object that loads a module.',
}

for nerd_word in nerd_words:
    print(f"'{nerd_word}' is {nerd_words[nerd_word]}")