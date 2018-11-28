
# coding: utf-8

# In[2]:


from userclass import User

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

