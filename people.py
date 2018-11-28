
# coding: utf-8

# # 6-1: Person

# In[3]:


person = {
    "first_name" : "tanner",
    "last_name" : "quinn",
    "age" : 22,
    "city" : "seattle"}
print(person["first_name"].title())
print(person["last_name"].title())
print(str(person["age"]))
print(person["city"].title())


# # 6-7: People
# 

# In[35]:


person = {
    "first_name" : "tanner",
    "last_name" : "quinn",
    "age" : 22,
    "city" : "seattle"}
person1 = {
    "first_name" : "elizabeth",
    "last_name" : "stewart",
    "age" : 23,
    "city" : "chicago"}
person2 = {
    "first_name" : "katherine",
    "last_name" : "ashmore",
    "age" : 53,
    "city" : "troy"}

peoples = [person, person1, person2]

for people in peoples:
    print("\nI know the following about you:")
    print("\n First name: " + people["first_name"].title() + "\t Last name: " + people["last_name"].title() 
          + "\t Age: " + str(people["age"]) + "\t City: " + people["city"].title())
    
    
    

