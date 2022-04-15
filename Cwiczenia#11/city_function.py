def get_formatted_city_country(city, country, population=''):
    """Generate a string with City and country and optionnaly population."""
    if population:
        formatted_city = f"{city.title()}, {country.title()} - population \
{population}."
    else:
        formatted_city = f"{city.title()}, {country.title()}."
    return formatted_city

    