
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
        
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
            
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges: 
            print("Administrator privileges: ")
            for privilege in self.privileges:
                print(" - " + privilege)
        else:
            print("You are not an administrator!")

