def get_city(city,country,population=""):
    """Returns formatted string with city and country name and population"""
    if population:
        formatted_name = f"{city},{country} - population {population}"
    else:
        formatted_name = f"{city},{country}"

    return formatted_name.title()



