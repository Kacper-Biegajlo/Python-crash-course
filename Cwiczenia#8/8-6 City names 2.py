## 8-6. City Names: 
# 
# Write a function called city_country() that takes in the name of a 
#   city and its country. 
# 
# The function should return a string formatted like this:
# "Santiago, Chile"
#
# Call your function with at least three city-country pairs, 
#   and print the values that are returned.

def city_country(city, country):
    """Returns a string with city name and it's country name."""
    city_country_formatted = f"{city}, {country}"

    print(city_country_formatted.title())

city_country('Warsaw', 'Poland')

city_country('Paris', 'France')

city_country('London', 'England')