
# coding: utf-8

# # 5-8: Hello Admin

# In[9]:


users = ["admin", "jerry", "barb", "kenny", "sally"]

for user in users:
    if user == "admin":
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again!")


# # 5-9: No Users
# 

# In[1]:


users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again!")
else:
    print("We need to find some users!")

