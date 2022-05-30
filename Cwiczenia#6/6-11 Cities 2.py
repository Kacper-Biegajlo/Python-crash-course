## 6-11. Cities: 

# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country 
#   that the city is in, its approximate population, 
#       and one fact about that city. 
# The keys for each city’s dictionary should be something like country, 
#   population, and fact. 
# Print the name of each city and all of 
#   the information you have stored about it.

cities = {
    'Warsaw': {
        'country': 'Poland',
        'population': '1.765 milion',
        'fact': 'Kaczor used to live there',
        },
    'Biała Podlaska': {
        'country': 'Poland',
        'population': '59.280 thousands',
        'fact': 'greatest city in the world',
        },
    'Pepega': {
        'country': 'Sadge',
        'population': '69',
        'fact': "it does not even exist",
        },
}

for city, city_info in cities.items():
    print(f"\nFew informations regaring {city.title()}:")
    print(f"Location: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fun fact: {city_info['fact'].title()}")