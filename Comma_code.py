#!/usr/bin/env python
# coding: utf-8

# In[89]:


def comma_code(spam):
    if len(spam) > 1:
       print(", ".join(spam[:-1]) + " and " + spam[-1])
    else:
        print(spam[0])
comma_code(["bananas","apples","tofu","cats"])


# In[91]:


def comma(spam):
    print(*spam[:-1], sep = ",", end = " ")
    print("and", spam[-1])
comma (["a","b","c"])
    

