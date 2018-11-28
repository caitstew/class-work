
# coding: utf-8

# In[ ]:


class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.location = location
    def describe_user(self):
        print("Full name: " + self.first_name.title() + " " + self.last_name.title())
        print("Age: " + self.age)
        print("Location: " + self.location.title())
    def greet_user(self):
        print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")
        

