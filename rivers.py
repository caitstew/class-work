
# coding: utf-8

# # 6-5: Rivers

# In[17]:


rivers = {
    "nile" : "egypt",
    "mississippi" : "usa", 
    "amazon" : "peru",
}
for river, country in rivers.items():
    if country == "usa":
        print("The " + river.title() + " runs through " + country.upper() + ".")
    else:
        print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print("\n" + river.title())
for country in rivers.values():
    if country == "usa":
        print("\n" + country.upper())
    else:
        print("\n" + country.title())

