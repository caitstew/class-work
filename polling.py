
# coding: utf-8

# # 6-6: Polling

# In[14]:


favorite_languages = {
    "jen" : "python", 
    "sarah" : "c", 
    "edward" : "ruby", 
    "phil" : "python",
}

new_poll = ["tanner", "jon", "edward", "caitlin", "christy", "sarah"]

print("You should all take my poll if you haven't already!")

for name in new_poll:
    if name in favorite_languages.keys():
        print("\n" + name.title() + ", I already have a recorded response from you.")
        print("I know your favorite language is " + language.title() + ".")
    else:
        print("\n" + name.title() + ", I do not yet know your favorite programming language.")

