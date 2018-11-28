
# coding: utf-8

# # 6-11: Cities

# In[8]:


cities = {"paris" : { "population" : "2.2 million", "country" : "france", "fact" : "It has the Eiffel Tower."},
        "london" : {"population" : "8.1 million", "country" : "england", "fact" : "It has Buckingham Palace."},
         "barcelona" : {"population" : "1.6 million", "country" : "spain", "fact" : "It has Barcelona Cathedral."}
         }
for city_name, city_info in cities.items():
    print("\nI love " + city_name.title() + "!")
    print("\nI know the following information about " + city_name.title() + ":")
    
    population = city_info["population"]
    country = city_info["country"]
    fact = city_info["fact"]
    
    print("\tPopulation: " + population)
    print("\tCountry: " + city)
    print("\tFact: " + fact)
    

