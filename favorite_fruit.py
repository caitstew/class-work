
# coding: utf-8

# # 5-7: Favorite Fruit

# In[2]:


favorite_fruits = ["raspberry", "mango", "pear"]
fruit = "raspberry"
if fruit in favorite_fruits:
    print("\nYou really love the fruit: " + fruit)
fruit = "pear"
if fruit in favorite_fruits:
    print("\nYou really love the fruit: " + fruit)
fruit = "mango"
if fruit in favorite_fruits:
    print("\nYou really love the fruit: " + fruit)
fruit = "pineapple"
if fruit not in favorite_fruits:
    print("\n" + fruit.title() + "s are not your favorite.")
fruit = "banana"
if fruit not in favorite_fruits:
    print("\n" + fruit.title() + "s are not your favorite.")

