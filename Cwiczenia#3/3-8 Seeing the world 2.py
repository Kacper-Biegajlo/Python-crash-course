## 3-8. Seeing the World ##

# Think of at least five places in the world you’d like to visit.

# - Store the locations in a list.
#       Make sure the list is not in alphabetical order.

# - Print your list in its original order. Don’t worry about printing the 
#       list neatly, just print it as a raw Python list.

# - Use sorted() to print your list in alphabetical order 
#       without modifying the actual list.

# - Show that your list is still in its original order by printing it.

# - Use sorted() to print your list in reverse alphabetical order 
#       without changing the order of the original list.

# - Show that your list is still in its original order by printing it again.

# - Use reverse() to change the order of your list. 
#       Print the list to show that its order has changed.

# - Use reverse() to change the order of your list again. 
#       Print the list to show it’s back to its original order.

# - Use sort() to change your list so it’s stored in alphabetical order. 
#       Print the list to show that its order has been changed.

# - Use sort() to change your list so it’s stored in reverse alphabetical order. 
#       Print the list to show that its order has changed.

Places = ['Moscov', 'Kyoto', 'Tokyo', 'Saint Petersburg', 'Chicago', 'New York']

print("\n",Places)

print("\n","Here is the list temporarly sorted by alphabetical order:",\
"\n",sorted(Places))

print("\n","Here is a proof that list is still in original order:",\
"\n",Places)

Places.reverse()
print("\n","Here is the list in the reverse order:","\n",Places)

Places.reverse()
print("\n","Here is the list reversed again so its back to orignal:",\
"\n",Places)

Places.sort()
print("\n","Here is the list sorted permamently in the alphabetical order:",\
"\n",Places)

Places.sort(reverse=True)
print("\n","Here is the list sorted permamently in the reverse alphabetical\
 order:","\n",Places)
