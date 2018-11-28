
# coding: utf-8

# # 5-2: More Conditional Tests

# ### Tests for equality and inequality with strings

# In[19]:



shoes = "sneakers"
shoes == "sneakers"


# In[20]:


shoes = "sneakers"
shoes == "ballet flats"


# ### Tests using the lower() function

# In[21]:


dad = "Michael"
dad.lower() == "michael"


# In[22]:


dad = "Michael"
dad.lower() == "Greg"


# ### Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

# In[23]:


Age = 16
Age >= 16


# In[24]:


Age = 22
Age < 16


# ### Tests using the *and* keyword and the *or* keyword

# In[25]:


shoesize = 7
shoesize2 = 9
shoesize > 6 and shoesize2 < 10


# In[30]:


pantsize = 26
pantsize2 = 30
(pantsize < 24) or (pantsize2 > 32)


# ### Test whether an item is in a list

# In[31]:


flowers = ["daisy", "tulip", "rose", "chrysanthemum"]
"chrysanthemum" in flowers


# In[32]:


trees = ["oak", "cedar", "maple"]
"gingko" in trees


# ### Test whether an in item is not in a list

# In[35]:


flowers = ["daisy", "tulip", "rose", "chrysanthemum"]
flower = "chrysanthemum" 
if flower not in flowers:
    print(flower + " is not in bouquet.")
else:
    print( flower.title() + "s are in the bouquet!")


# In[37]:


trees = ["oak", "cedar", "maple"]
tree = "gingko" 
if tree not in trees:
    print("I'm sorry, there are no " + tree + " trees in my yard.")

