#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[36]:


class tempConvert:
    "A class to convert temperatures between Celsius, Fahrenheit, and Kelvin"
    
    def FtoC(temp):
        "Converting Fahrenheit to Celsius"
        
        templist = []
        
        for i in temp:
            templist.append(round(((i - 32.) * (5./9.)), 2))
            
        return templist
    
    def CtoF(temp):
        "Converting Celsius to Fahrenheit"
        
        templist = []
        
        for i in temp:
            templist.append(round((i * (9./5.) + 32.), 2))
            
        return templist
    
    def CtoK(temp):
        "Converting Celsius to Kelvin"
        
        templist = []
        
        for i in temp:
            templist.append(round((i + 273.15), 2))
            
        return templist
    
    def KtoC(temp):
        "Converting Kelvin to Celsius"
        
        templist = []
        
        for i in temp:
            templist.append(round((i - 273.15), 2))
            
        return templist
    
    def FtoK(temp):
        "Converting Fahrenheit to Kelvin"
        
        templist = []
        
        for i in temp:
            templist.append(round(((i - 32.) * (5./9.) - 273.15), 2))
            
        return templist
    
    def KtoF(temp):
        "Converting Kelvin to Fahrenheit"
        
        templist = []
        
        for i in temp:
            templist.append(round(((i + 273.15) * (9./5.) + 32.), 2))
            
        return templist
    


# In[40]:


temps = [15.,20.,25.,30.,40.]

f = tempConvert.FtoC(temps)


# In[38]:


f


# In[39]:


g = tempConvert.KtoC(temps)
g

