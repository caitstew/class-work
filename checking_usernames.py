
# coding: utf-8

# # 5-10: Checking Usernames

# In[6]:


current_users = ["bob", "joe", "harry", "maggie", "stuart"]
new_users = ["henry", "freeda", "stuart", "JOE", "lin"]
for new_user in new_users: 
    if new_user.lower() in current_users:
        print("The username " + new_user + ", is already taken. Please enter a new username.")
    else:
        print("The username " + new_user + ", is available!")

