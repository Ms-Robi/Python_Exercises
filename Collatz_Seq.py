#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3 * number + 1

#Program
try:
 userInput = int(input("Enter number: "))
 while userInput != 1:
       userInput = collatz(userInput)
       print(userInput)  
    
except: 
    print("Error: Invalid, enter numbers only!") 
    
 

