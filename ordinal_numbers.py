
# coding: utf-8

# # 5-11: Ordinal Numbers

# In[3]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number > 3:
        print(str(number) + "th")
    elif number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")

