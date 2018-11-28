
# coding: utf-8

# # 6-5: Glossary

# In[4]:


terms = {
        "concatenation" : "combining strings",
        "strings" : "a series of characters. Anything inside quotes is considered a string in Python",
        "list" : "a collection of items in a particular order", 
        "set" : "a collection of items where the order does not matter", 
        "loop" : "allows you to take the same action or a set of actions, with every item in a list",
}

for term, definition in terms.items():
    print("\n" + term.title() + " can be defined as: \n" + definition.title() + ".")

