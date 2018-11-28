
# coding: utf-8

# # 7-5: Movie Tickets

# In[9]:


prompt = "How old are you? "

age = input(prompt)

if int(age) < 3:
    print(str("Your ticket is free!"))
elif int(age) <= 12:
    print(str("Your ticket is $10.00."))
else:
    print(str("Your ticket is $15.00."))


#  # 7-6: Three Exits

# In[2]:


prompt = "For each member in your party enter their age: "
prompt += "\nWhen you have entered every person's age enter 'done'."



while True:
    age = input(prompt)

    if age == "done":
        break
        print("\nYou have entered all age information for your party.")
    elif int(age) < 3:
        print(str("\nThat person's ticket is free!"))
    elif int(age) <= 12:
        print(str("\nThat person's ticket is $10.00."))
    else:
        print(str("\nThat person's ticket is $15.00."))


# In[4]:


prompt = "For each member in your party enter their age: "
prompt += "\nWhen you have entered every person's age enter 'done'."

active = True

while active:
    age = input(prompt)

    if age == "done":
        break
        print("\nYou have entered all age information for your party.")
    elif int(age) < 3:
        print(str("\nThat person's ticket is free!"))
    elif int(age) <= 12:
        print(str("\nThat person's ticket is $10.00."))
    else:
        print(str("\nThat person's ticket is $15.00."))


# In[2]:


prompt = "For each member in your party enter their age: "
prompt += "\nWhen you have entered every person's age enter 'done'."

while prompt != "done":
    age = input(prompt)
    if int(age) < 3:
        print(str("\nThat person's ticket is free!"))
    elif int(age) <= 12:
        print(str("\nThat person's ticket is $10.00."))
    else:
        print(str("\nThat person's ticket is $15.00."))

