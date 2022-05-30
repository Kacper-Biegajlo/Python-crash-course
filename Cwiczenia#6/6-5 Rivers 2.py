##  6-5. Rivers: 

# Make a dictionary containing three major rivers and the country each 
#   river runs through. One key-value pair might be 'nile': 'egypt'.

# * Use a loop to print a sentence about each river,
#    such as The Nile runs through Egypt.

# * Use a loop to print the name of each river included in the dictionary.

# * Use a loop to print the name of each country included in the dictionary.

rivers = {
    'wisła': 'poland',
    'loire': 'france',
    'main': 'germany'
    }

for river, country in rivers.items():
    print(f"{river.title()} is main river of {country.title()}.")

print("\nMain rivers in alphabetical order:")
for river in sorted(rivers.keys()):
    print(river.title())

print("\nCountries in alphabetical order:")
for country in sorted(rivers.values()):
    print(country.title())