
# coding: utf-8

# # 6-8: Pets

# In[17]:


foster = {"name" : "foster",
          "owner" : "katherine", 
         "breed" : "golden retriever",}
bailey = {"name" : "bailey",
          "owner" : "michael", 
         "breed" : "norwegian forest cat",}
jojo = {"name" : "jojo",
        "owner" : "caitlin", 
         "breed" : "long-haired american cat"}

pets = [foster, bailey, jojo]

print("This is what I know about our pet families:")
for pet in pets:
    print("\n" + pet["name"].title() + "'s owner is " + pet["owner"].title() + ". " 
          + pet["name"].title() + " is a " + pet["breed"] + ".")

