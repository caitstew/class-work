
# coding: utf-8

# # 6-2: Favorite Numbers

# In[3]:


favorite_numbers = {
    "Beth" : 34, 
    "Karl" : 78,
    "Roman" : 2,
    "Grace" : 7, 
    "Claire" : 16,
}
print("Beth's favorite number is " + str(favorite_numbers["Beth"]) + "!")
print("Karl's favorite number is " + str(favorite_numbers["Karl"]) + "!")
print("Roman's favorite number is " + str(favorite_numbers["Roman"]) + "!")
print("Grace's favorite number is " + str(favorite_numbers["Grace"]) + "!")
print("Claire's favorite number is " + str(favorite_numbers["Claire"]) + "!")


# # 6-10: Favorite Numbers

# In[17]:


favorite_numbers = {
    "Beth" : [34, 42, 65, 1],
    "Karl" : [78, 84, 2, 0],
    "Roman" : [2, 3, 4],
    "Grace" : [7, 5], 
    "Claire" : [16, 100, 45],
}
for name, numbers in favorite_numbers.items():
    print(name + "'s favorite numbers are: ")
    for number in numbers:
        print(str(number))

