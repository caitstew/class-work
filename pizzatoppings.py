
# coding: utf-8

# # 7-4: Pizza Toppings

# In[1]:


prompt = "Enter all the toppings you would like on your pizza: "
prompt += "\nEnter 'done' when you have added all the topping you would like."

while True:
    toppings = input(prompt)
    
    if toppings == "done":
        break
    else:
        print("\nAdding " + toppings + " to your pizza!")

