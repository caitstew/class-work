def city_function(city, country, population= ''):
    if population:
        output = city.title() + ", " + country.title() + " - population: " + str(population)
    else: 
        output = city.title() + ", " + country.title()
    return output


