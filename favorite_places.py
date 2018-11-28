
# coding: utf-8

# # 6-9: Favorite Places

# In[16]:


favorite_places = {"caitlin" : ["iceland", "australia", "spain"], 
                  "michael" : ["ecuador", "galapagos islands", "brazil"],
                   "elizabeth" : ["japan", "germany", "denmark"],
                  }
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())
    
    

