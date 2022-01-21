#!/usr/bin/env python
# coding: utf-8

# In[20]:


""" Create a function displayInventory that takes a dictionary and displays the items as follows:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62 """


def displayInventory(inv):
    total_items = 0
    print("Inventory:")
    
    for key,value in inv.items():
        print(value,key)
        total_items = total_items + value
        
    print("Total number of items: %d" %total_items)
    
#Add loot from dragonLoot to inventory

def addToInventory(invtry, addedItems):
    for loot in dragonLoot:
        if loot in invtry:
            invtry[loot] += 1
        else:
            invtry[loot] = 1
    return(invtry)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

addToInventory(inventory, dragonLoot)
displayInventory(inventory)

