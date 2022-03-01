## More Conditional Tests: You don’t have to limit the number of tests you 
#   create to ten. 

# If you want to try more comparisons, 
#   write more tests and add them to conditional_tests.py. 
#       Have at least one True and one False result for each of the following:

# * Tests for equality and inequality with strings

polish_cities = ['warsaw', 'krakov', 'lublin']
fav_city = 'munich'

if fav_city not in polish_cities:
    print(f"{fav_city.title()} is not a polish city.")
if fav_city in polish_cities:
    print(f"{fav_city.title()} is a polish city.")

# acttually I think I did most of tests in this and previous file
