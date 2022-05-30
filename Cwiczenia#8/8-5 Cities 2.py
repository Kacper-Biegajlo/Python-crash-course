## 8-5. Cities: 
# 
# Write a function called describe_city() that accepts the name 
#   of a city and its country. 
# 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# 
# Give the parameter for the country a default value. 
# 
# Call your function for three different cities, at least one of which 
#   is not in the default country.

def describe_city(city_name, city_country='Poland'):
    print(f"City called '{city_name}' is located in {city_country}.")

describe_city('Warsaw')

describe_city(city_name='Karków')

describe_city(city_name='Berlin', city_country='Germany')