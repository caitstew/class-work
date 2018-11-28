
# coding: utf-8

# In[ ]:


class Restuarant():
    def __init__(self, name, cuisine_type, number_served):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restuarant(self):
        print("You want to have " + self.cuisine_type.title() + " food at the resturant, " 
              + self.name.title() + ".")
    def open_restuarant(self):
        print("The restaurant, " + self.name.title() + ", is open!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, customers):
        self.number_served += customers

